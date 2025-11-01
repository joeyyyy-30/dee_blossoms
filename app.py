from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_flower', methods=['POST'])
def get_flower():
    emotion = request.form['emotion'].lower()

    flower_data = {
        'happy': ('Sunflower 🌻', 
                  "Dee, your happiness lights up everything around you — like a sunflower chasing the sun’s warmth.", 
                  '/static/images/happy.jpg',
                  "P.S. Never stop smiling; it’s my favorite view."),
        'sad': ('Blue Iris 💙', 
                "Even in your softest moments, Dee, you hold beauty and strength — like a blue iris blooming after the rain.", 
                '/static/images/sad.jpg',
                "P.S. It’s okay to feel — even clouds rest before shining again."),
        'loved': ('Rose 🌹', 
                  "Dee, you’re love itself — timeless, pure, and breathtaking, just like the rose.", 
                  '/static/images/rose.jpg',
                  "P.S. You’ll always be loved, endlessly."),
        'relaxed': ('Lavender 💜', 
                    "Peace looks perfect on you, Dee — calm, comforting, and graceful like lavender fields in the breeze.", 
                    '/static/images/lavender.jpg',
                    "P.S. You deserve every bit of peace the world can offer."),
        'energetic': ('Marigold 🧡', 
                      "You radiate warmth and fire, Dee — just like marigolds that never stop glowing under the sun.", 
                      '/static/images/marigold.jpg',
                      "P.S. You’re unstoppable — never dim that spark."),
        'romantic': ('Jasmine 🤍', 
                     "Dee, your heart carries the softness of jasmine — subtle yet unforgettable in its beauty.", 
                     '/static/images/jasmine.jpg',
                     "P.S. You make love itself feel poetic."),
        'strong': ('Hibiscus ❤️', 
                   "Dee, you bloom with courage and grace — bold and beautiful like the hibiscus.", 
                   '/static/images/hibiscus.jpg',
                   "P.S. You’re proof that gentle souls can also be powerful."),
        'grateful': ('Peony 🌸', 
                     "Gratitude flows through you, Dee — full and radiant, like peonies dancing in spring.", 
                     '/static/images/penoy.jpg',
                     "P.S. You make even the smallest moments feel special."),
        'creative': ('Orchid 💜', 
                     "Your creativity is rare and enchanting, Dee — like an orchid that thrives in its own magic.", 
                     '/static/images/orchid.jpg',
                     "P.S. Keep creating beauty; the world needs more of you."),
        'stressed': ('White Lily 🤍', 
                     "Dee, even when life feels heavy, remember — lilies still bloom through the calm after the storm.", 
                     '/static/images/lily.jpg',
                     "P.S. Breathe, you’ve got this — always."),
        'confident': ('Tulip 🌷', 
                      "Dee, you walk with quiet confidence — like tulips standing tall, owning their place in the sun.", 
                      '/static/images/tulip.jpg',
                      "P.S. You’re doing better than you think."),
        'hopeful': ('Daffodil 💛', 
                    "Dee, your hope shines bright — like daffodils bringing color after a long winter.", 
                    '/static/images/daffodil.jpg',
                    "P.S. The best days are yet to come."),
        'caring': ('Carnation 💖', 
                   "Your kindness is a soft strength, Dee — like carnations that bring comfort without even trying.", 
                   '/static/images/carnation.jpg',
                   "P.S. The world’s gentler because of you."),
        'peaceful': ('Cherry Blossom 🌸', 
                     "Dee, your presence feels like spring — calm, quiet, and breathtaking, like cherry blossoms in the wind.", 
                     '/static/images/cherry_blossom.jpg',
                     "P.S. Stay still sometimes — the world moves beautifully around you."),
        'focused': ('Chrysanthemum 💛', 
                    "Dee, your focus is golden — steady and bright, like chrysanthemums that stand proud and clear.", 
                    '/static/images/chrysanthemum.jpg',
                    "P.S. Keep your eyes on your dreams; they’re waiting for you.")
    }

    # Fallback for unknown emotions
    flower_name, message, image_path, ps_line = flower_data.get(
        emotion,
        ("🌼 Unknown Emotion 🌼",
         "I couldn’t find a flower for that feeling, Dee — but you’re always special in every way. 💖",
         "/static/images/daisy.jpg",
         "P.S. Maybe the flower just hasn’t met your mood yet.")
    )

    return render_template('result.html', 
                           flower_name=flower_name, 
                           message=message, 
                           image_path=image_path,
                           ps_line=ps_line)

# Serve sitemap.xml for Google indexing
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

# Serve Google Search Console verification file
# (Replace the filename below with your actual Google file name, e.g., google1234abcd.html)
@app.route('/google1234abcd.html')
def google_verify():
    return send_from_directory('.', 'google1234abcd.html')

if __name__ == '__main__':
    app.run(debug=True)
