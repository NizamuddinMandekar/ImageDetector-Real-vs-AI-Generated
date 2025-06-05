<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Detector - AI Image Detector</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: 
                radial-gradient(circle at 20% 20%, rgba(255, 0, 150, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(0, 255, 255, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 60%, rgba(255, 100, 0, 0.2) 0%, transparent 50%),
                linear-gradient(135deg, #0a0a0a 0%, #1a0033 25%, #003366 50%, #330066 75%, #000000 100%);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
            animation: backgroundShift 20s ease-in-out infinite;
        }

        /* Animated background particles */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            background: 
                radial-gradient(circle at 10% 10%, rgba(255, 0, 255, 0.4) 0%, transparent 30%),
                radial-gradient(circle at 90% 90%, rgba(0, 255, 255, 0.4) 0%, transparent 30%),
                radial-gradient(circle at 50% 50%, rgba(255, 255, 0, 0.2) 0%, transparent 40%);
            animation: rotate 30s linear infinite;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg) scale(1); }
            50% { transform: rotate(180deg) scale(1.1); }
            100% { transform: rotate(360deg) scale(1); }
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float 8s ease-in-out infinite;
            box-shadow: 0 0 6px rgba(255, 255, 255, 0.6);
        }

        @keyframes backgroundShift {
            0%, 100% { 
                filter: hue-rotate(0deg) brightness(1); 
            }
            25% { 
                filter: hue-rotate(90deg) brightness(1.1); 
            }
            50% { 
                filter: hue-rotate(180deg) brightness(0.9); 
            }
            75% { 
                filter: hue-rotate(270deg) brightness(1.1); 
            }
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            text-align: center;
            margin-bottom: 2rem;
            animation: slideInDown 1s ease-out;
        }

        .title {
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(45deg, #ff0080, #00ffff, #ffff00, #ff8000, #8000ff);
            background-size: 500% 500%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 2s ease-in-out infinite, titleGlow 3s ease-in-out infinite alternate;
            margin-bottom: 1rem;
            text-shadow: 0 0 50px rgba(255, 255, 255, 0.3);
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            25% { background-position: 100% 0%; }
            50% { background-position: 100% 100%; }
            75% { background-position: 0% 100%; }
        }

        @keyframes titleGlow {
            0% { 
                filter: drop-shadow(0 0 20px rgba(255, 0, 128, 0.8)) drop-shadow(0 0 40px rgba(0, 255, 255, 0.6));
                transform: scale(1);
            }
            100% { 
                filter: drop-shadow(0 0 30px rgba(255, 255, 0, 0.8)) drop-shadow(0 0 50px rgba(128, 0, 255, 0.6));
                transform: scale(1.02);
            }
        }

        .subtitle {
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 0.5rem;
        }

        .accuracy-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            color: white;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.3);
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .description-section {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(30px);
            border-radius: 25px;
            padding: 2rem;
            margin-bottom: 3rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            box-shadow: 
                0 15px 35px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 0 50px rgba(255, 0, 128, 0.1);
            max-width: 1000px;
            width: 100%;
            animation: fadeInUp 1s ease-out 0.3s both;
        }

        .description-section h2 {
            color: #00ffff;
            font-size: 1.8rem;
            margin-bottom: 1rem;
            text-align: center;
            font-weight: 700;
        }

        .description-section h3 {
            color: #ffff00;
            font-size: 1.3rem;
            margin: 1.5rem 0 1rem 0;
            font-weight: 600;
        }

        .description-section p {
            color: rgba(255, 255, 255, 0.9);
            line-height: 1.6;
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        .description-section ul, .description-section ol {
            color: rgba(255, 255, 255, 0.85);
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }

        .description-section li {
            margin-bottom: 0.5rem;
            line-height: 1.5;
        }

        .description-section strong {
            color: #ff8000;
            font-weight: 600;
        }

        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            width: 100%;
            max-width: 1000px;
            animation: fadeInUp 1s ease-out 0.5s both;
        }

        .upload-section, .results-section {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(30px);
            border-radius: 25px;
            padding: 2rem;
            border: 2px solid rgba(255, 255, 255, 0.1);
            box-shadow: 
                0 15px 35px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2),
                0 0 50px rgba(255, 0, 128, 0.1);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .upload-section::before, .results-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.6s ease;
        }

        .upload-section:hover::before, .results-section:hover::before {
            left: 100%;
        }

        .upload-section:hover, .results-section:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 
                0 25px 50px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.3),
                0 0 80px rgba(0, 255, 255, 0.2);
            border-color: rgba(255, 255, 255, 0.3);
        }

        .section-title {
            font-size: 1.5rem;
            color: white;
            margin-bottom: 1.5rem;
            text-align: center;
            font-weight: 600;
        }

        .upload-area {
            border: 2px dashed rgba(255, 255, 255, 0.5);
            border-radius: 15px;
            padding: 3rem 2rem;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .upload-area:hover {
            border-color: rgba(255, 255, 255, 0.8);
            background: rgba(255, 255, 255, 0.1);
        }

        .upload-area.dragover {
            border-color: #4ecdc4;
            background: rgba(78, 205, 196, 0.1);
            transform: scale(1.02);
        }

        .upload-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: rgba(255, 255, 255, 0.8);
            animation: bounce 2s ease-in-out infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .upload-text {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }

        .file-input {
            display: none;
        }

        .upload-btn {
            background: linear-gradient(45deg, #ff0080, #00ffff, #ffff00, #ff8000);
            background-size: 300% 300%;
            color: white;
            border: none;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.4s ease;
            box-shadow: 
                0 8px 25px rgba(255, 0, 128, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
            animation: buttonGlow 3s ease-in-out infinite alternate;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .upload-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 
                0 15px 35px rgba(255, 0, 128, 0.6),
                inset 0 1px 0 rgba(255, 255, 255, 0.4);
            background-position: 100% 0%;
        }

        @keyframes buttonGlow {
            0% { 
                box-shadow: 
                    0 8px 25px rgba(255, 0, 128, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3);
                background-position: 0% 50%;
            }
            100% { 
                box-shadow: 
                    0 8px 25px rgba(0, 255, 255, 0.4),
                    inset 0 1px 0 rgba(255, 255, 255, 0.3);
                background-position: 100% 50%;
            }
        }

        .image-preview {
            max-width: 100%;
            max-height: 300px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            margin-bottom: 1rem;
            animation: imageAppear 0.5s ease-out;
        }

        @keyframes imageAppear {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }

        .results-container {
            text-align: center;
        }

        .prediction-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: resultSlide 0.5s ease-out;
        }

        @keyframes resultSlide {
            from { opacity: 0; transform: translateX(30px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .prediction-label {
            font-size: 1.2rem;
            font-weight: 600;
            color: white;
            margin-bottom: 0.5rem;
        }

        .confidence-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
            border-radius: 4px;
            transition: width 1s ease-out;
            animation: fillBar 1s ease-out;
        }

        @keyframes fillBar {
            from { width: 0%; }
        }

        .confidence-text {
            color: rgba(255, 255, 255, 0.9);
            font-size: 0.9rem;
        }

        .processing {
            display: none;
            text-align: center;
            color: white;
            font-size: 1.1rem;
        }

        .spinner {
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid #4ecdc4;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .examples-section {
            margin-top: 3rem;
            text-align: center;
            animation: fadeInUp 1s ease-out 1s both;
        }

        .examples-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .example-img {
            width: 100%;
            height: 120px;
            object-fit: cover;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }

        .example-img:hover {
            transform: scale(1.05);
            border-color: #4ecdc4;
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);
        }

        .footer-section {
            margin-top: 3rem;
            text-align: center;
            padding: 2rem;
            animation: fadeInUp 1s ease-out 1.2s both;
        }

        .article-credit {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1rem;
            font-weight: 500;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            display: inline-block;
        }

        @keyframes slideInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            
            .title {
                font-size: 2.5rem;
            }
            
            .container {
                padding: 1rem;
            }

            .description-section {
                padding: 1.5rem;
            }

            .description-section h2 {
                font-size: 1.5rem;
            }

            .description-section h3 {
                font-size: 1.1rem;
            }
        }
    </style>
</head>
<body>
    <div class="bg-animation"></div>
    
    <div class="container">
        <div class="header">
            <h1 class="title">Image Detector</h1>
            <p class="subtitle">AI-Powered Image Authenticity Detector</p>
            <span class="accuracy-badge">✨ 95% Accuracy</span>
        </div>

        <!-- Description Section -->
        <div class="description-section">
            <h2>AI Image Detector: Real Vs Fake Faces.</h2>
            <h3>Important Guidelines:</h3>
            <ul>
                <li><strong>Focus on Faces:</strong> Ensure the uploaded images clearly show faces. The model is optimized for facial recognition and classification.</li>
                <li><strong>Image Examples:</strong> Refer to the examples below to understand the type of images suitable for classification.</li>
                <li><strong>Avoid Other AI-Generated Content:</strong> Do not upload images of objects, landscapes, or any non-facial AI-generated content as the model is not trained to classify these correctly.</li>
            </ul>
            <h3>Usage Instructions:</h3>
            <ol>
                <li><strong>Prepare Your Image:</strong> Ensure the face is visible and prominent.</li>
                <li><strong>Upload the Image:</strong> Use the provided interface to upload your image for classification.</li>
                <li><strong>Receive Classification:</strong> The model will analyze the facial features and classify the image as either real or fake with 95% accuracy.</li>
            </ol>
            <p>Start using the model now to see the power of AI in distinguishing between real and AI-generated faces!</p>
        </div>

        <div class="main-content">
            <div class="upload-section">
                <h2 class="section-title">Upload Image</h2>
                <div class="upload-area" id="uploadArea">
                    <div class="upload-icon">📷</div>
                    <p class="upload-text">Drag & drop an image here or click to browse</p>
                    <button class="upload-btn" onclick="document.getElementById('fileInput').click()">
                        Choose File
                    </button>
                    <input type="file" id="fileInput" class="file-input" accept="image/*">
                </div>
                <div id="imagePreview" style="display: none; margin-top: 1rem; text-align: center;">
                    <img id="previewImg" class="image-preview" alt="Preview">
                </div>
            </div>

            <div class="results-section">
                <h2 class="section-title">Analysis Results</h2>
                <div class="results-container">
                    <div class="processing" id="processing">
                        <div class="spinner"></div>
                        <p>Analyzing image...</p>
                    </div>
                    
                    <div id="results" style="display: none;">
                        <div class="prediction-card">
                            <div class="prediction-label">Real Image</div>
                            <div class="confidence-bar">
                                <div class="confidence-fill" id="realBar" style="width: 0%"></div>
                            </div>
                            <div class="confidence-text" id="realConfidence">0%</div>
                        </div>
                        
                        <div class="prediction-card">
                            <div class="prediction-label">AI Generated</div>
                            <div class="confidence-bar">
                                <div class="confidence-fill" id="fakeBar" style="width: 0%"></div>
                            </div>
                            <div class="confidence-text" id="fakeConfidence">0%</div>
                        </div>
                        
                        <div style="margin-top: 1rem; color: rgba(255, 255, 255, 0.8);">
                            <small>Processing time: <span id="processTime">0.00s</span></small>
                        </div>
                    </div>
                    
                    <div id="noResults" style="color: rgba(255, 255, 255, 0.7);">
                        Upload an image to see analysis results
                    </div>
                </div>
            </div>
        </div>

        <div class="examples-section">
            <h2 class="section-title">Try These Examples</h2>
            <div class="examples-grid" id="examplesGrid">
                <!-- Example images will be loaded here -->
            </div>
        </div>

        <!-- Footer Section -->
        <div class="footer-section">
            <p class="article-credit">Created by Nizamuddin Mandekar</p>
        </div>
    </div>

    <script>
        // Create animated background particles
        function createParticles() {
            // Particles removed - clean background with just gradient effects
        }

        // File upload handling
        const fileInput = document.getElementById('fileInput');
        const uploadArea = document.getElementById('uploadArea');
        const imagePreview = document.getElementById('imagePreview');
        const previewImg = document.getElementById('previewImg');
        const processing = document.getElementById('processing');
        const results = document.getElementById('results');
        const noResults = document.getElementById('noResults');

        // Drag and drop functionality
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                handleFile(files[0]);
            }
        });

        uploadArea.addEventListener('click', () => {
            fileInput.click();
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                handleFile(e.target.files[0]);
            }
        });

        function handleFile(file) {
            if (!file.type.startsWith('image/')) {
                alert('Please select an image file');
                return;
            }

            const reader = new FileReader();
            reader.onload = (e) => {
                previewImg.src = e.target.result;
                imagePreview.style.display = 'block';
                analyzeImage();
            };
            reader.readAsDataURL(file);
        }

        function analyzeImage() {
            // Hide previous results
            results.style.display = 'none';
            noResults.style.display = 'none';
            
            // Show processing animation
            processing.style.display = 'block';

            // Simulate analysis (replace with actual API call)
            setTimeout(() => {
                const realConfidence = Math.random() * 0.4 + 0.3; // 30-70%
                const fakeConfidence = 1 - realConfidence;

                // Hide processing
                processing.style.display = 'none';
                
                // Show results
                results.style.display = 'block';
                
                // Update confidence bars and text
                const realPercentage = Math.round(realConfidence * 100);
                const fakePercentage = Math.round(fakeConfidence * 100);
                
                document.getElementById('realBar').style.width = realPercentage + '%';
                document.getElementById('fakeBar').style.width = fakePercentage + '%';
                document.getElementById('realConfidence').textContent = realPercentage + '%';
                document.getElementById('fakeConfidence').textContent = fakePercentage + '%';
                document.getElementById('processTime').textContent = (Math.random() * 2 + 0.5).toFixed(3) + 's';
                
            }, 2000);
        }

        // Load example images (placeholder)
        function loadExamples() {
            const examplesGrid = document.getElementById('examplesGrid');
            const exampleUrls = [
                'https://picsum.photos/150/120?random=1',
                'https://picsum.photos/150/120?random=2',
                'https://picsum.photos/150/120?random=3',
                'https://picsum.photos/150/120?random=4'
            ];

            exampleUrls.forEach((url, index) => {
                const img = document.createElement('img');
                img.src = url;
                img.className = 'example-img';
                img.alt = `Example ${index + 1}`;
                img.onclick = () => {
                    previewImg.src = url;
                    imagePreview.style.display = 'block';
                    analyzeImage();
                };
                examplesGrid.appendChild(img);
            });
        }

        // Initialize
        createParticles();
        loadExamples();
    </script>
</body>
</html>
