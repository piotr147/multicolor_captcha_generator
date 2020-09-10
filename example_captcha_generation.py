#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####################################################################################################

from img_captcha_gen import CaptchaGenerator
from os import path, makedirs

####################################################################################################

# Path to generate Captchas
GEN_CAPTCHAS_FOLDER = "./captchas"

# Captcha image size number (2 -> 640x360)
CAPCTHA_SIZE_NUM = 3

NUMBER_OF_CAPTCHAS_TO_GENERATE = 5

####################################################################################################

# Main Function #

def main():
    '''Main Function'''
    # Create Captcha Generator object of specified size
    CaptchaGen = CaptchaGenerator(CAPCTHA_SIZE_NUM)
    # If it doesn't exists, create captchas folder to store generated captchas
    if not path.exists(GEN_CAPTCHAS_FOLDER):
        makedirs(GEN_CAPTCHAS_FOLDER)
    # Generate 20 captchas
    for i in range(0, NUMBER_OF_CAPTCHAS_TO_GENERATE):
        Chars_mode="nums"
        Shapes=True
        Noise=False
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="nums"
        Shapes=False
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="nums"
        Shapes=True
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="letters"
        Shapes=True
        Noise=False
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="letters"
        Shapes=False
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="letters"
        Shapes=True
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="numsletters"
        Shapes=True
        Noise=False
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="numsletters"
        Shapes=False
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

        Chars_mode="numsletters"
        Shapes=True
        Noise=True
        captcha = CaptchaGen.gen_captcha_image(chars_mode=Chars_mode, shapes=Shapes, noise=Noise)
        saveCaptcha(captcha, Chars_mode, Shapes, Noise)

    print("Process completed. Check captchas images at \"{}\" folder.".format(GEN_CAPTCHAS_FOLDER))

def getFolderName(chars_mode, shapes, noise):
    name = "./captchas/" + chars_mode
    if shapes:
        name = name + "Shapes"
    if noise:
        name = name + "Noise"

    return name

def saveCaptcha(captcha, chars_mode, shapes, noise):
    directory = getFolderName(chars_mode, shapes, noise)
    image = captcha["image"]
    characters = captcha["characters"]
    print("Generated captcha {}: {}".format(directory, characters))
    if not path.exists(directory):
        makedirs(directory)
    image.save("{}/{}.png".format(directory, characters), "png")


if __name__ == '__main__':
    main()
