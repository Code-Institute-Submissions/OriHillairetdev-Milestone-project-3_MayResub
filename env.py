import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "MagicalCatMan")
os.environ.setdefault(
    "MONGO_URI",
    "mongodb+srv://Ori_dev:Wolf777@book-nook.ofwaf.mongodb.net/ \
        BookNook?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "BookNook")
