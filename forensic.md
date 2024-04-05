# Forensic

| **Files analyse**|
`exiftool flie_name`analyse image metadata |
| `steghide extract -sf file_name` | extracte infos |
| `ltrace` |  vérifier le nombre exact d'octets qu'un binaire de défi tente de lire |
| `diff passwords.old passwords.new` | difference between 2 files |
## _extracte embeded info_
```
binwalk --run-as=root -e file
```

extracte encripted zip
```
7z x file.zip -p'passwd'
```
| `grep -oE '\b\w{4}\b' fichier.txt` | filter for 4 letters |

# pcap file
**filtrer les packets et extraire les données**
```
tshark -r file.pcap -Y 'filter' -T field -e data
```

# ps snoop
## **pspy** 

# data analyze
|   |   |
|---|---|
| `hexdump -C data_file` |  |
| `hexeditor ` |  |
| `strings file` | extract data file's strings |

# image
## _Contenu d'un fichier PNG minimal représentant un pixel rouge_
![[Capture d’écran du 2023-08-11 06-43-10.png]]
## _pngcheck_
vérifie l'intégrité des fichiers PNG, JNG et MNG (en vérifiant les CRC 32 bits internes, c'est-à-dire les sommes de contrôle, et en décompressant les données d'image) ; il peut éventuellement vider presque toutes les informations au niveau du bloc dans l'image sous une forme lisible par l'homme. Par exemple, il peut être utilisé pour imprimer les statistiques de base sur une image (dimensions, profondeur de bits, etc.) ; pour répertorier les informations de couleur et de transparence dans sa palette (en supposant qu'il en ait une); ou pour extraire les annotations de texte incorporées. Il s'agit d'un programme en ligne de commande avec des capacités de traitement par lots.
```
pngcheck -cvt file.png
```

## _msb/lsb_
```
pip install Pillow
wget https://raw.githubusercontent.com/Pulho/sigBits/master/sigBits.py
python3 sigBits.py file.png
```

```
python3 sigBits.py file.png
cat outputSB.txt | grep -o -E "message.{0,50}"
```

## jpeg list marker
HEX	MARKER	MARKER NAME	DESCRIPTION
0x FFC0	SOF0	Start of Frame 0	Baseline DCT
0x FFC1	SOF1	Start of Frame 1	Extended Sequential DCT
0x FFC2	SOF2	Start of Frame 2	Progressive DCT
0x FFC3	SOF3	Start of Frame 3	Lossless (sequential)
0x FFC4	DHT	Define Huffman Table	
0x FFC5	SOF5	Start of Frame 5	Differential sequential DCT
0x FFC6	SOF6	Start of Frame 6	Differential progressive DCT
0x FFC7	SOF7	Start of Frame 7	Differential lossless (sequential)
0x FFC8	JPG	JPEG Extensions	
0x FFC9	SOF9	Start of Frame 9	Extended sequential DCT, Arithmetic coding
0x FFCA	SOF10	Start of Frame 10	Progressive DCT, Arithmetic coding
0x FFCB	SOF11	Start of Frame 11	Lossless (sequential), Arithmetic coding
0x FFCC	DAC	Define Arithmetic Coding	
0x FFCD	SOF13	Start of Frame 13	Differential sequential DCT, Arithmetic coding
0x FFCE	SOF14	Start of Frame 14	Differential progressive DCT, Arithmetic coding
0x FFCF	SOF15	Start of Frame 15	Differential lossless (sequential), Arithmetic coding
0x FFD0	RST0	Restart Marker 0	
0x FFD1	RST1	Restart Marker 1	
0x FFD2	RST2	Restart Marker 2	
0x FFD3	RST3	Restart Marker 3	
0x FFD4	RST4	Restart Marker 4	
0x FFD5	RST5	Restart Marker 5	
0x FFD6	RST6	Restart Marker 6	
0x FFD7	RST7	Restart Marker 7	
0x FFD8	SOI	Start of Image	
0x FFD9	EOI	End of Image	
0x FFDA	SOS	Start of Scan	
0x FFDB	DQT	Define Quantization Table	
0x FFDC	DNL	Define Number of Lines	(Not common)
0x FFDD	DRI	Define Restart Interval	
0x FFDE	DHP	Define Hierarchical Progression	(Not common)
0x FFDF	EXP	Expand Reference Component	(Not common)
0x FFE0	APP0	Application Segment 0	JFIF – JFIF JPEG image
AVI1 – Motion JPEG (MJPG)
0x FFE1	APP1	Application Segment 1	EXIF Metadata, TIFF IFD format,
JPEG Thumbnail (160×120)
Adobe XMP
0x FFE2	APP2	Application Segment 2	ICC color profile,
FlashPix
0x FFE3	APP3	Application Segment 3	(Not common)
JPS Tag for Stereoscopic JPEG images
0x FFE4	APP4	Application Segment 4	(Not common)
0x FFE5	APP5	Application Segment 5	(Not common)
0x FFE6	APP6	Application Segment 6	(Not common)
NITF Lossles profile
0x FFE7	APP7	Application Segment 7	(Not common)
0x FFE8	APP8	Application Segment 8	(Not common)
0x FFE9	APP9	Application Segment 9	(Not common)
0x FFEA	APP10	Application Segment 10
PhoTags	(Not common)
ActiveObject (multimedia messages / captions)
0x FFEB	APP11	Application Segment 11	(Not common)
HELIOS JPEG Resources (OPI Postscript)
0x FFEC	APP12	Application Segment 12	Picture Info (older digicams),
Photoshop Save for Web: Ducky
0x FFED	APP13	Application Segment 13	Photoshop Save As: IRB, 8BIM, IPTC
0x FFEE	APP14	Application Segment 14	(Not common)
0x FFEF	APP15	Application Segment 15	(Not common)
0x FFF0 …
0x FFF6	JPG6	JPEG Extension 0 …
JPEG Extension 6	(Not common)
0x FFF7	JPG7
SOF48	JPEG Extension 7
JPEG-LS	Lossless JPEG
0x FFF8	JPG8
LSE	JPEG Extension 8
JPEG-LS Extension	Lossless JPEG Extension Parameters
0x FFF9	JPG9	JPEG Extension 9	(Not common)
0x FFFA	JPG10	JPEG Extension 10	(Not common)
0x FFFB	JPG11	JPEG Extension 11	(Not common)
0x FFFC	JPG12	JPEG Extension 12	(Not common)
0x FFFD	JPG13	JPEG Extension 13	(Not common)
0x FFFE	COM	Comment
