#!/usr/bin/env python

import sys
import nibabel as nib

# Giriş dosyasını yükleyip başlık (header) bilgisini output.txt'ye yaz
img = nib.load(sys.argv[1])
with open("output.txt", "w") as f:
    f.write(str(img.header))
    