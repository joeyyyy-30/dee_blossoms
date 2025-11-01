from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_flower', methods=['POST'])
def get_flower():
    emotion = request.form['emotion'].lower()

    flower_data = {
        'happy': ('Sunflower 🌻', "Dee, your joy lights up every space like a sunflower turning toward the sun — radiant, warm, and full of life.", '/static/images/happy.jpg'),
        'sad': ('Blue Iris 💙', "Even in sadness, Dee, there’s beauty in your heart — gentle, deep, and strong like the iris that blooms in the rain.", '/static/images/sad.jpg'),
        'loved': ('Rose 🌹', "You’re cherished beyond words, Dee — as timeless and beautiful as a rose in full bloom.", '/static/images/rose.jpg'),
        'relaxed': ('Lavender 💜', "Calm suits you, Dee — like lavender fields at dusk, peaceful and endlessly graceful.", '/static/images/lavender.jpg'),
        'energetic': ('Marigold 🧡', "Your energy glows bright and warm, Dee — like marigolds chasing the sunlight, fearless and full of color.", '/static/images/marigold.jpg'),
        'romantic': ('Jasmine 🤍', "Your charm is soft yet unforgettable, Dee — like jasmine’s scent in the night, tender and eternal.", '/static/images/jasmine.jpg'),
        'strong': ('Hibiscus ❤️', "Strength blooms in you, Dee — bold, beautiful, and unshaken like the hibiscus under the summer sun.", '/static/images/hibiscus.jpg'),
        'grateful': ('Peony 🌸', "Your heart carries thankfulness like peonies in bloom — full, gentle, and radiant with grace.", '/static/images/penoy.jpg'),
        'creative': ('Orchid 💜', "Your creativity, Dee, is rare and breathtaking — like the orchid that thrives where others can’t.", '/static/images/orchid.jpg'),
        'stressed': ('White Lily 🤍', "Lilies whisper peace, Dee — breathe, relax, and remember you’re never alone in your storms.", '/static/images/lily.jpg'),
        'confident': ('Tulip 🌷', "You carry yourself with quiet confidence, Dee — like tulips that rise proud after the frost.", '/static/images/tulip.jpg'),
        'hopeful': ('Daffodil 💛', "Hope blooms within you, Dee — bright and golden, just like daffodils greeting a new spring.", '/static/images/daffodil.jpg'),
        'caring': ('Carnation 💖', "Your caring heart softens every moment, Dee — gentle and true like a field of carnations.", '/static/images/carnation.jpg'),
        'peaceful': ('Cherry Blossom 🌸', "Like cherry blossoms, Dee, your calm spirit brings beauty and peace wherever it drifts.", '/static/images/cherry_blossom.jpg'),
        'focused': ('Chrysanthemum 💛', "Your focus is golden, Dee — unwavering, steady, and full of quiet brilliance like chrysanthemums in bloom.", '/static/images/chrysanthemum.jpg')
    }

    # Fallback for unknown emotions
    flower_name, message, image_path = flower_data.get(
        emotion,
        ("🌼 Unknown Emotion 🌼",
         "I couldn’t find a flower for that feeling, Dee — but you’re always special. 💖",
         "/static/images/daisy.jpg")
    )

    # PS line appears under the image in the template
    ps_line = "P.S. I’ll get you these flowers soon 🌷"

    return render_template('result.html', flower_name=flower_name, message=message, image_path=image_path, ps_line=ps_line)


# 🌸 Optional Google Search Console Verification Route
@app.route('/google<file_id>.html')
def google_verification(file_id):
    return send_from_directory('static', f'google{file_id}.html')


if __name__ == '__main__':
    app.run(debug=True)
