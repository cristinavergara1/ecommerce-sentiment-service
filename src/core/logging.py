import logging
import sys
from typing import Optional

def configure_logging(level: Optional[str] = None) -> None:
    """
    Configura el sistema de logging para la aplicación.
    
    Args:
        level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    log_level = level or "INFO"
    
    # Configurar el formato de los logs
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configurar el logger raíz
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Configurar loggers específicos para reducir ruido
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("transformers").setLevel(logging.WARNING)
    logging.getLogger("torch").setLevel(logging.WARNING)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging configurado con nivel: {log_level}")

configure_logging()