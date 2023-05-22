from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
fluffy = Pet(name='Fluffy', species='Dog', photo_url='https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', age=2, notes='Playful', available=True)

butters = Pet(name='Butters', species='Cat',
              photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg', age=3, notes='Weird', available=True)

bentley = Pet(name='Bentley', species='Dog',
              photo_url='https://media-be.chewy.com/wp-content/uploads/2021/04/18143927/iStock-1453345538-616x615.jpg', age=1, notes='Loves to jump on you', available=False)

hammy = Pet(name='Hammy', species='Hamster',
            photo_url='https://media.istockphoto.com/id/675804830/photo/beige-hamster.jpg?s=612x612&w=0&k=20&c=e4P9Z3U3PVwtNEMZUCkoDkBrHr9E0XDxk9fZdDKZHZ4=', age=0.5, notes='Small', available=True)

tony = Pet(name='Tony', species='Parrot', photo_url='https://lafeber.com/pet-birds/wp-content/uploads/2020/04/gamaliel-troubleson-u9PsLITXMCQ-unsplash-e1587001975887.jpg',
           age=5, notes='Talkative and annoying', available=False)

# Add new objects to session, so they'll persist
db.session.add(fluffy)
db.session.add(butters)
db.session.add(bentley)
db.session.add(hammy)
db.session.add(tony)

# Commit--otherwise, this never gets saved!
db.session.commit()
