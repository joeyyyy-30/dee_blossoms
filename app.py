from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_flower', methods=['POST'])
def get_flower():
    emotion = request.form['emotion'].lower()

    flower_data = {
        'happy': ('Sunflower 🌻',
                  "Dee, you are a sunflower — always turning toward the light, brightening everything around you just by existing.",
                  '/static/images/happy.jpg'),

        'sad': ('Blue Iris 💙',
                "Dee, you are a blue iris — even when you bend under the rain, your beauty never fades. You carry grace in your quiet tears.",
                '/static/images/sad.jpg'),

        'loved': ('Rose 🌹',
                  "Dee, you are the rose — timeless, radiant, and impossible to forget. Love doesn’t just surround you; it *blooms* from you.",
                  '/static/images/rose.jpg'),

        'relaxed': ('Lavender 💜',
                    "Dee, you are lavender — soothing, soft, and full of peace. Even silence feels beautiful when you’re in it.",
                    '/static/images/lavender.jpg'),

        'energetic': ('Marigold 🧡',
                      "Dee, you are a marigold — glowing, fiery, and unstoppable. The world feels more alive when you’re near.",
                      '/static/images/marigold.jpg'),

        'romantic': ('Jasmine 🤍',
                     "Dee, you are jasmine — delicate, enchanting, and quietly unforgettable. You don’t try to shine, you just *do*.",
                     '/static/images/jasmine.jpg'),

        'strong': ('Hibiscus ❤️',
                   "Dee, you are a hibiscus — bold and full of life. Strength and beauty bloom together in your spirit.",
                   '/static/images/hibiscus.jpg'),

        'grateful': ('Peony 🌸',
                     "Dee, you are a peony — layered with warmth and grace. Gratitude isn’t something you say; it’s something you *are*.",
                     '/static/images/penoy.jpg'),

        'creative': ('Orchid 💜',
                     "Dee, you are an orchid — rare, elegant, and endlessly expressive. The world feels more inspired when you touch it.",
                     '/static/images/orchid.jpg'),

        'stressed': ('White Lily 🤍',
                     "Dee, you are a white lily — pure, calm, and made to bring peace. Even when the world feels heavy, your soul stays gentle.",
                     '/static/images/lily.jpg'),

        'confident': ('Tulip 🌷',
                      "Dee, you are a tulip — graceful, bold, and effortlessly sure of yourself. You don’t follow the light, you *create* it.",
                      '/static/images/tulip.jpg'),

        'hopeful': ('Daffodil 💛',
                    "Dee, you are a daffodil — a reminder that light always returns. You make hope look effortless.",
                    '/static/images/daffodil.jpg'),

        'caring': ('Carnation 💖',
                   "Dee, you are a carnation — soft, warm, and full of love that lingers long after you leave. You make people feel safe.",
                   '/static/images/carnation.jpg'),

        'peaceful': ('Cherry Blossom 🌸',
                     "Dee, you are a cherry blossom — fleeting yet unforgettable. Your calmness paints the world in quiet pinks and peace.",
                     '/static/images/cherry_blossom.jpg'),

        'focused': ('Chrysanthemum 💛',
                    "Dee, you are a chrysanthemum — steady, thoughtful, and full of quiet determination. Even your stillness has purpose.",
                    '/static/images/chrysanthemum.jpg')
    }

    # Fallback for unknown emotions
    flower_name, message, image_path = flower_data.get(
        emotion,
        ("🌼 Unknown Emotion 🌼",
         "I couldn’t find a flower for that feeling, Dee — but I know you’d still outshine them all.",
         "/static/images/daisy.jpg")
    )

    ps_line = "P.S. I’ll get you real flowers soon 🌸"

    return render_template(
        'result.html',
        flower_name=flower_name,
        message=message,
        image_path=image_path,
        ps_line=ps_line
    )

if __name__ == '__main__':
    app.run(debug=True)
