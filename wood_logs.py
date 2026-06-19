import pygame
from config import LOG_SIZES

# Preloaded log sprites for different size variants.
# Each entry contains a scaled version of the same base image.
# This allows consistent rendering of logs with different lengths.
logs_dict = { }

log_img = pygame.image.load("images/log.png")

logs_dict["short"] = pygame.transform.scale(log_img, LOG_SIZES["short"])
logs_dict["medium"] = pygame.transform.scale(log_img, LOG_SIZES["medium"])
logs_dict["long"] = pygame.transform.scale(log_img, LOG_SIZES["long"])