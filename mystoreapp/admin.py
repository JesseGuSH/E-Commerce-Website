from flask import Blueprint
from . import db
from .models import Category, Product

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
    c1 = Category(name='IndoorPlants', image='indoorPlants.jpg')
    c2 = Category(name='OutdoorPlants', image='outdoorPlants.jpg')
    c3 = Category(name='PotsAccessories', image='potsAccessories.jpg')
      
    try:
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    p1 = Product(category_id=c1.id, image='P1_dracaena-golden-heart_Indoor.jpg', price=79,\
        name='Dracaena Golden Heart',\
        description= 'The Dracaena Golden Heart is one of the easiest indoor plants around. The brightly striped leaves of this plant will flourish and adapt to almost any indoor environment. With glossy green to yellow foliage, this upright tropical houseplant thrives as a low-light interior plant and even adapts to fluorescent lighting. Also able to grow well in indirect bright light, the foliage will lighten in color.The Dracaena Golden Heart is native to tropical regions of Africa.')
    
    p2 = Product(category_id=c1.id, image='P2_bamboo-palm_stone_Indoor.jpg', price=160,\
        name='Bamboo Palm',\
        description= 'The Bamboo Palm is a tropical indoor houseplant that compliments any space. Not to be confused with real bamboo, this plant is low maintenance and easy to care for.Native to the forests of Mexico and Central America, Bamboo Palms grow in the shade of larger trees unlike other palms, which makes them adaptable to less-than-ideal lighting conditions. It is a great choice for the home or office because it rates highly on NASA’s list of air-purifying plants.')

    p3 = Product(category_id=c1.id,image='P3_bird-of-paradise_Indoor.jpg',price=600,\
        name='Bird of Paradise Tree',\
        description='You don’t need to leave your house to be on vacation with the iconic Bird of Paradise, now bigger and better than ever. The common name comes from the vibrant white and purple flowers that resemble a tropical bird. When grown indoors, it will not have enough light to produce a bloom. However, the majestic foliage and graceful stems make a statement on their own.<br>The Bird of Paradise is native to the warm climate of South Africa, where it receives plenty of natural light and humidity. ')

    p4 = Product(category_id=c2.id,image='P4_Large_MandevillaTrellisRed_Outdoor.jpg',price=600,\
        name='Mandevilla Pink Red',\
        description='You don’t need to leave your house to be on vacation with the iconic Bird of Paradise, now bigger and better than ever. The common name comes from the vibrant white and purple flowers that resemble a tropical bird. When grown indoors, it will not have enough light to produce a bloom. However, the majestic foliage and graceful stems make a statement on their own.The Bird of Paradise is native to the warm climate of South Africa, where it receives plenty of natural light and humidity. ')
    
    p5 = Product(category_id=c2.id,image='P5_LRG_MandevillaTrellisPink_Outdoor.jpg',price=149,\
        name='Mandevilla Pink',\
        description='The trumpet-shaped blooms of the Mandevilla are undoubtedly the highlight of this outdoor tropical plant. Blooming continuously throughout the summer, the plant becomes covered in large pink flowers for a show stopping effect. This plant requires minimal maintenance — just full sun, regular feeding, and the occasional trim of any wayward vines.')
    
    p6 = Product(category_id=c2.id,image='P6_Magnolia_grandiflora_Teddy_Bear_Outdoor.jpg',price=245,\
        name='Magnolia grandiflora - Teddy Bear',\
        description='The Magnolia grandiflora Teddy Bear is a stunning evergreen shrub that produces large, fragrant white flowers in the summer, with a compact and bushy growth habit. Its manageable size and year-round interest make it a perfect choice for any landscape, adding a touch of elegance and beauty to any garden.')
    
    p7 = Product(category_id=c3.id,image='P7_wooden-plant-stand_PotsAccessories.jpg',price=50,\
        name='Wooden Plant Stand',\
        description='Inspired by the minimalist, mid-century modern designs of the 1950s, this Wooden Plant Stand is adjustable to allow for plant pots of varied widths between 8-12 inches. It pairs beautifully with our large and extra large plants and comes in three timeless colors, Natural, Black, and Dark Brown.')

    p8 = Product(category_id=c3.id,image='P8_RepottingKit_Medium_Stone_PotsAccessories.jpg',price=60,\
        name='Repotting Kit (10” Pot)',\
        description='Is your plant showing signs of being root-bound and needing a larger pot? Repot your foliage friend with our Repotting Kit. This kit comes with one 10” round Ecopot and one 8-quart bag of our premium potting soil. It’s perfect for plants that have outgrown an 8” pot.')
    
    p9 = Product(category_id=c3.id,image='P9_complete-gardening-tool-set-scaled-PotsAccessories.jpg',price=130,\
        name='Complete Gardening Tool Set',\
        description='Our Complete Gardening Tool Set includes everything you need for pruning, harvesting, trimming, repotting, and planting. An ideal gift for the budding avid gardener to set them up for a successful long-term relationship caring for their plants.')

    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'