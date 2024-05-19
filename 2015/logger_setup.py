import logging


def setup_logging(log_level):
    """
    Set up logging configuration.

    Parameters:
    log_level (str): Desired log level as a string (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],
    )
