import qrcode
from io import BytesIO
from appwrite.services.storage import Storage
from appwrite_client import get_client

def handler(req, res):
    client = get_client()
    storage = Storage(client)
    
    data = req.json
    shortened_url = data.get('shortenedURL')
    url_id = data.get('urlID')
    
    qr_code_data = generate_qr_code(shortened_url)
    
    file_data = BytesIO(qr_code_data)
    file_data.name = f'qr-{url_id}.png'
    
    result = storage.create_file('bucketId', file_data, ['role:all'])
    
    res.json({'qrCodeFileURL': result['$id']})

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    return byte_io.getvalue()
