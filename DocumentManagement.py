from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

# To be changed with DB
UPLOAD_FOLDER = 'path_to_your_upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/documents/upload', methods=['POST'])
def upload_document():
    if 'document' not in request.files:
        return jsonify({'message': 'No document part in the request'}), 400

    file = request.files['document']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        # Generate a unique "document ID"
        document_id = str(uuid.uuid4())
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], document_id + "_" + filename)
        file.save(save_path)

        # Would likely want to start a background job for processing the document after saving it

        return jsonify({'message': 'File uploaded successfully', 'documentId': document_id}), 201


if __name__ == '__main__':
    app.run(debug=True)
