"""Content generation engine using LangChain and Ollama with GPU support"""

import os
import requests
import json
from typing import Optional, List, Dict, Any
from langchain_community.llms import Ollama
from prompts import PromptBuilder

# Enable GPU acceleration if available
os.environ['OLLAMA_NUM_GPU'] = '1'  # Use GPU
os.environ['OLLAMA_NUM_THREAD'] = str(os.cpu_count() or 8)  # Use max CPU threads


class OllamaManager:
    """Manage Ollama model connections and operations"""

    OLLAMA_BASE_URL = "http://localhost:11434"
    DEFAULT_MODEL = "llama3"
    AVAILABLE_MODELS = ["llama3", "mistral", "gemma", "phi3", "neural-chat"]

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.base_url = self.OLLAMA_BASE_URL

    @staticmethod
    def is_ollama_running() -> bool:
        """Check if Ollama server is running"""
        try:
            response = requests.get(
                f"{OllamaManager.OLLAMA_BASE_URL}/api/tags", timeout=2
            )
            return response.status_code == 200
        except (requests.ConnectionError, requests.Timeout):
            return False

    @staticmethod
    def get_available_models() -> List[str]:
        """Get list of available models on Ollama server"""
        try:
            response = requests.get(
                f"{OllamaManager.OLLAMA_BASE_URL}/api/tags", timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                models = [model["name"].split(":")[0] for model in data.get("models", [])]
                return list(set(models))
        except Exception:
            pass
        return []

    @staticmethod
    def pull_model(model_name: str) -> bool:
        """Pull a model from Ollama (requires manual intervention)"""
        return True  # User should run: ollama run <model_name>

    def test_connection(self) -> bool:
        """Test connection to Ollama with current model"""
        if not self.is_ollama_running():
            return False

        try:
            llm = Ollama(model=self.model, base_url=self.base_url)
            response = llm.invoke("Say 'OK' only")
            return response.strip().upper() == "OK"
        except Exception:
            return False

    def set_model(self, model_name: str):
        """Set the model to use"""
        self.model = model_name

    def get_current_model(self) -> str:
        """Get current model"""
        return self.model

    def get_gpu_status(self) -> Dict[str, Any]:
        """Check if model is running on GPU or CPU by querying Ollama"""
        try:
            # First, try to get actual model info from Ollama
            response = requests.post(
                f"{self.OLLAMA_BASE_URL}/api/show",
                json={"name": self.model},
                timeout=5
            )
            
            gpu_info = {
                "model": self.model,
                "is_gpu_available": False,
                "status": "Checking...",
                "environment": {
                    "OLLAMA_NUM_GPU": os.environ.get('OLLAMA_NUM_GPU', '0'),
                    "OLLAMA_NUM_THREAD": os.environ.get('OLLAMA_NUM_THREAD', 'auto'),
                }
            }
            
            if response.status_code == 200:
                data = response.json()
                details = data.get("details", {})
                
                # Check details for GPU information
                gpu_info["architecture"] = details.get("architecture", "unknown")
                gpu_info["parameters"] = data.get("parameters", "")
                
                # Check Ollama version and capabilities
                try:
                    version_response = requests.get(
                        f"{self.OLLAMA_BASE_URL}/api/version",
                        timeout=5
                    )
                    if version_response.status_code == 200:
                        version_info = version_response.json()
                        gpu_info["ollama_version"] = version_info.get("version", "unknown")
                except:
                    pass
                
                # Determine GPU status - check if Ollama was started with GPU support
                # This is indicated by OLLAMA_NUM_GPU environment variable
                gpu_enabled_in_env = os.environ.get('OLLAMA_NUM_GPU', '0') != '0'
                
                if gpu_enabled_in_env:
                    gpu_info["is_gpu_available"] = True
                    gpu_info["status"] = "🟢 GPU ACCELERATION ENABLED (Ollama should use GPU)"
                    gpu_info["note"] = "GPU was enabled when Ollama started"
                else:
                    gpu_info["is_gpu_available"] = False
                    gpu_info["status"] = "🔴 GPU DISABLED - Running on CPU only"
                    gpu_info["note"] = "To enable GPU, restart Ollama with GPU support enabled"
                
                return gpu_info
                
            else:
                gpu_info["status"] = "⚠️ Could not detect GPU status"
                gpu_info["is_gpu_available"] = False
                return gpu_info
                
        except Exception as e:
            return {
                "status": f"❌ Error checking GPU: {str(e)}",
                "is_gpu_available": False,
                "note": "Make sure Ollama is running",
                "environment": {
                    "OLLAMA_NUM_GPU": os.environ.get('OLLAMA_NUM_GPU', '0'),
                    "OLLAMA_NUM_THREAD": os.environ.get('OLLAMA_NUM_THREAD', 'auto'),
                }
            }

    def enable_gpu(self) -> bool:
        """Enable GPU acceleration (requires Ollama restart)"""
        try:
            os.environ['OLLAMA_NUM_GPU'] = '1'
            os.environ['OLLAMA_NUM_THREAD'] = str(os.cpu_count() or 8)
            return True
        except Exception:
            return False

    def disable_gpu(self) -> bool:
        """Disable GPU acceleration (requires Ollama restart)"""
        try:
            os.environ['OLLAMA_NUM_GPU'] = '0'
            return True
        except Exception:
            return False


class ContentGenerator:
    """Generate content using Ollama and LangChain"""

    def __init__(self, ollama_manager: OllamaManager = None):
        if ollama_manager is None:
            ollama_manager = OllamaManager()
        self.ollama_manager = ollama_manager
        self.timeout = 300  # 5 minutes timeout

    def _get_llm(self, temperature: float = 0.7):
        """Get LangChain LLM instance"""
        return Ollama(
            model=self.ollama_manager.get_current_model(),
            base_url=self.ollama_manager.base_url,
            temperature=temperature,
        )

    def generate_content(
        self,
        content_type: str,
        topic: str,
        audience: str,
        tone: str,
        style: str,
        length: str,
        language: str,
        keywords: str,
        creativity: float = 0.7,
        num_outputs: int = 1,
    ) -> List[str]:
        """Generate content based on parameters"""

        prompt_text = PromptBuilder.build_prompt(
            content_type=content_type,
            topic=topic,
            audience=audience,
            tone=tone,
            style=style,
            length=length,
            language=language,
            keywords=keywords,
            creativity=creativity,
        )

        llm = self._get_llm(temperature=creativity)

        outputs = []
        for i in range(num_outputs):
            try:
                response = llm.invoke(prompt_text)
                if response and response.strip():
                    outputs.append(response.strip())
            except Exception as e:
                raise ValueError(f"Error generating content: {str(e)}")

        return outputs if outputs else ["Error: No content generated. Please try again."]

    def rewrite_content(
        self, original_text: str, rewrite_type: str, tone: str = None, style: str = None
    ) -> str:
        """Rewrite existing content"""

        prompt_text = PromptBuilder.build_rewrite_prompt(
            original_text=original_text,
            rewrite_type=rewrite_type,
            tone=tone,
            style=style,
        )

        llm = self._get_llm(temperature=0.5)

        try:
            response = llm.invoke(prompt_text)
            return response.strip() if response else original_text
        except Exception as e:
            raise ValueError(f"Error rewriting content: {str(e)}")

    def enhance_content(self, original_text: str, enhancement_type: str) -> str:
        """Enhance existing content"""

        prompt_text = PromptBuilder.build_enhancement_prompt(
            original_text=original_text, enhancement_type=enhancement_type
        )

        llm = self._get_llm(temperature=0.6)

        try:
            response = llm.invoke(prompt_text)
            return response.strip() if response else original_text
        except Exception as e:
            raise ValueError(f"Error enhancing content: {str(e)}")

    def generate_from_template(
        self, template_text: str, placeholders: dict, creativity: float = 0.7
    ) -> str:
        """Generate content from template with placeholders"""

        filled_template = template_text
        for placeholder, value in placeholders.items():
            filled_template = filled_template.replace(f"{{{placeholder}}}", value)

        llm = self._get_llm(temperature=creativity)

        prompt_text = f"""Based on this template, generate complete content:

{filled_template}

Important: Generate ONLY the content, no explanations."""

        try:
            response = llm.invoke(prompt_text)
            return response.strip() if response else filled_template
        except Exception as e:
            raise ValueError(f"Error generating from template: {str(e)}")

    def batch_generate(
        self, prompts: List[str], temperature: float = 0.7
    ) -> List[str]:
        """Generate multiple outputs from multiple prompts"""

        llm = self._get_llm(temperature=temperature)
        outputs = []

        for prompt in prompts:
            try:
                response = llm.invoke(prompt)
                if response:
                    outputs.append(response.strip())
            except Exception:
                outputs.append("")

        return outputs

    def get_model_info(self) -> dict:
        """Get information about current model including GPU status"""
        gpu_status = self.ollama_manager.get_gpu_status()
        return {
            "model": self.ollama_manager.get_current_model(),
            "base_url": self.ollama_manager.base_url,
            "is_running": self.ollama_manager.is_ollama_running(),
            "available_models": self.ollama_manager.get_available_models(),
            "gpu_status": gpu_status,
        }
