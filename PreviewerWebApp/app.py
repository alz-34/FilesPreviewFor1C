from flask import Flask, render_template, request
import os
import tempfile
import img2pdf
from shutil import copyfile
from converter import Converter

THIS_FOLDER             = os.path.dirname(os.path.abspath(__file__))
PREVIEW_FILES_STORAGE   = 'static/Files'
ALLOWED_FROM_EXTENSIONS = {'docx', 'xlsx', 'pdf', 'jpeg', 'jpg', 'png', 'tiff'}
ALLOWED_TO_EXTENSIONS   = {'odt', 'ods', 'pdf'}
IMG_SUPPORTED_EXT       = {'jpeg', 'jpg','png', 'tiff'}
UNOCONV                 = Converter()
CONV_MAP = {
    "docx": "odt pdf",
    "pdf": "pdf",
    'xlsx': "ods pdf",
    'jpeg': "pdf",
    'jpg': "pdf",
    'png': "pdf",
    'tiff': "pdf"    
}

app = Flask(__name__)


def get_filename(name, ext):
    return f'{name}.{ext}'


def abspath_for_save_file(filename):
    return f'{THIS_FOLDER}/{PREVIEW_FILES_STORAGE}/{filename}'


@ app.route('/test')
def test_page():
    return "Работает!"


@ app.route('/allowedExt')
def allowed_extensions():
    return ' '.join(map(str, ALLOWED_FROM_EXTENSIONS))


@ app.route('/allowedExt/<from_ext>')
def allowed_extensions_for_extension(from_ext):
    extList = [value for key, value in CONV_MAP.items() if from_ext == key]
    return ' '.join(map(str, extList))


@ app.route('/preview/<ext>/<fname>')
def show_in_viewer(ext, fname):
    _filename = get_filename(fname, ext)
    if os.path.isfile(abspath_for_save_file(_filename)):
        return render_template('preview.html', anchorUrl=f'../Files/{_filename}')
    else:
        return render_template('notFound.html', _filename=_filename), 404


@ app.route('/upload/<from_ext>/<to_ext>', methods=['POST'])
def upload_file(from_ext, to_ext):
    
    if request.method != 'POST':
        return "Неправильный запрос", 400
    
    if from_ext not in ALLOWED_FROM_EXTENSIONS:
        return f'Не поддерживается отображение файлов в формате {from_ext}', 400

    if to_ext not in ALLOWED_TO_EXTENSIONS:
        return f'Не поддерживается конвертация файла в формат {to_ext}', 400

    extList = [key for key, value in CONV_MAP.items() if to_ext in value]
    if len(extList) == 0:
        return f'Не поддерживается конвертация файла из формата {from_ext} в формат {to_ext}', 400

    return save_file(from_ext, to_ext), 201           


def save_file(from_ext, to_ext):
    newTmpFile = tempfile.NamedTemporaryFile(delete=False, suffix=f'.{from_ext}')
    try:
        newTmpFile.file.write(request.data)
        newTmpFile.file.close()  # windows problem, need to release file        
        tmpFilename = newTmpFile.name
        rmTmpFile = False
        if from_ext != to_ext:
            if from_ext in IMG_SUPPORTED_EXT:
                tmpFilename = convert_image_file(tmpFilename)                
            else:
                tmpFilename = convert_file(tmpFilename, to_ext)                
            rmTmpFile = True
        _newFilename = os.path.basename(tmpFilename)
        _dst = abspath_for_save_file(_newFilename)
        copyfile(tmpFilename, _dst)
        if rmTmpFile:
            os.remove(tmpFilename)
    finally:
        os.remove(newTmpFile.name)
    return _newFilename


def convert_file(absPathToFile, to_ext):
    UNOCONV.convert('-f', to_ext, absPathToFile)    
    return get_newAbsPathFromSourceAbsPath(absPathToFile, to_ext)

def convert_image_file(absPathToFile):
    newAbsPath = get_newAbsPathFromSourceAbsPath(absPathToFile, 'pdf')
    with open(newAbsPath,"wb") as f:
	        f.write(img2pdf.convert(absPathToFile))   
    return newAbsPath

def get_newAbsPathFromSourceAbsPath(absPathToFile, outputExt):    
    _basename = os.path.basename(absPathToFile)
    _filename = os.path.splitext(_basename)[0]   
    newFilename = f'{_filename}.{outputExt}'
    dirName = os.path.dirname(absPathToFile)    
    newAbsPath = os.path.join(dirName, newFilename)
    return newAbsPath

@ app.route('/delete/<ext>/<fname>')
def delete_file(ext, fname):
    _filename = get_filename(fname, ext)
    if os.path.isfile(abspath_for_save_file(_filename)):
        os.remove(abspath_for_save_file(_filename))
    return "ОК"


if __name__ == '__main__':
    app.run()
