from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# toistaiseksi saatavilla olevat kielet:
# kieliin, joissa käytetään erilaisia merkkejä on lisää paketteja ladattavissa.

"""print(pytesseract.get_languages(config=''))

['afr', 'amh', 'ara', 'asm', 'aze', 'aze_cyrl', 'bel', 'ben',
 'bod', 'bos', 'bre', 'bul', 'cat', 'ceb', 'ces', 'chi_sim',
 'chi_sim_vert', 'chi_tra', 'chi_tra_vert', 'chr', 'cos', 'cym',
 'dan', 'deu', 'deu_latf', 'div', 'dzo', 'ell', 'eng', 'enm',
 'epo', 'equ', 'est', 'eus', 'fao', 'fas', 'fil', 'fin', 'fra',
 'frm', 'fry', 'gla', 'gle', 'glg', 'grc', 'guj', 'hat', 'heb',
 'hin', 'hrv', 'hun', 'hye', 'iku', 'ind', 'isl', 'ita', 'ita_old',
 'jav', 'jpn', 'jpn_vert', 'kan', 'kat', 'kat_old', 'kaz', 'khm',
 'kir', 'kmr', 'kor', 'lao', 'lat', 'lav', 'lit', 'ltz', 'mal',
 'mar', 'mkd', 'mlt', 'mon', 'mri', 'msa', 'mya', 'nep', 'nld',
 'nor', 'oci', 'ori', 'osd', 'pan', 'pol', 'por', 'pus', 'que',
 'ron', 'rus', 'san', 'sin', 'slk', 'slv', 'snd', 'spa', 'spa_old',
 'sqi', 'srp', 'srp_latn', 'sun', 'swa', 'swe', 'syr', 'tam', 'tat',
 'tel', 'tgk', 'tha', 'tir', 'ton', 'tur', 'uig', 'ukr', 'urd', 'uzb',
 'uzb_cyrl', 'vie', 'yid', 'yor']
 """
 
image = Image.open('test_images/koira_runo.png')

gray_image = image.convert('L')

text = pytesseract.image_to_string(gray_image, lang='fin')

print(text)