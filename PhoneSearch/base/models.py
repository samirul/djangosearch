from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #pass

class phoneName(models.Model):
    names = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneName = models.CharField(max_length=200)
    avatar = models.ImageField(null=True, default = "image.png")

    def __str__(self):
        return self.phoneName
    
class Phone(models.Model):
    name = models.ForeignKey(phoneName, on_delete=models.CASCADE)
    network = models.CharField("NETWORK", max_length=200, default='NETWORK')  # Network
    technology = models.CharField("Technology", max_length=200, blank=True)
    twogBands = models.CharField("2G bands", max_length=200, blank=True)
    threegBands = models.CharField("3G bands", max_length=200, blank=True)
    fourgBands = models.CharField("4G bands", max_length=200, blank=True)
    fivegBands = models.CharField("5G bands", max_length=200, blank=True)
    speed = models.CharField("Speed", max_length=200, blank=True)

    launch = models.CharField("LAUNCH", max_length=200, default='LAUNCH') # LAUNCH
    announced = models.CharField("Announced", max_length=200, blank=True)
    status = models.CharField("Status", max_length=200, blank=True)

    body = models.CharField("BODY", max_length=200, default='BODY') # BODY
    dimensions = models.CharField("Dimensions", max_length=200, blank=True)
    weight = models.CharField("Weight", max_length=200, blank=True)
    build = models.CharField("Build", max_length=200, blank=True)
    sim = models.CharField("SIM", max_length=200, blank=True)
    rgb = models.CharField("RGB", max_length=200, blank=True)
    
    display = models.CharField("DISPLAY", max_length=200, default='DISPLAY') # DISPLAY
    typess = models.CharField("Type", max_length=200, blank=True)
    size = models.CharField("Size", max_length=200, blank=True)
    resolution = models.CharField("Resolution", max_length=200, blank=True)
    protection = models.CharField("Protection", max_length=200, blank=True)

    platform = models.CharField("PLATFORM", max_length=200, default='PLATFORM') # PLATFORM
    os = models.CharField("OS", max_length=200, blank=True)
    chipset = models.CharField("Chipset", max_length=200, blank=True)
    cpu = models.CharField("CPU", max_length=200, blank=True)
    gpu = models.CharField("GPU", max_length=200, blank=True)

    memory = models.CharField("MEMORY", max_length=200, default='MEMORY') # MEMORY
    cardSlot = models.CharField("Card slot", max_length=200, blank=True)
    internal = models.CharField("Internal", max_length=200, blank=True)
    storage = models.CharField("Storage", max_length=200, blank=True)

    mainCamera = models.CharField("MAIN CAMERA", max_length=200, default='MAIN CAMERA') # MAIN CAMERA
    dual = models.CharField("Dual/Triple", max_length=200, blank=True)
    mainfeatures = models.CharField("Features", max_length=200, blank=True)
    video = models.CharField("Video", max_length=200, blank=True)

    selfieCamera = models.CharField("SELFIE CAMERA", max_length=200, default='SELFIE CAMERA') # SELFIE CAMERA
    selfieSingle = models.CharField("Single", max_length=200, blank=True)
    selfieFeatures = models.CharField("Features", max_length=200, blank=True)
    selfieVideo = models.CharField("video", max_length=200, blank=True)

    sound = models.CharField("Sound", max_length=200, default='SOUND') # Sound
    loudspeakerS = models.CharField("Loudspeaker", max_length=200, blank=True)
    jack = models.CharField("3.5mm jack", max_length=200, blank=True)
    frequency = models.CharField("Sound Frequency", max_length=200, blank=True)

    comms = models.CharField("COMMS", max_length=200, default='COMMS') # COMMS
    wlan = models.CharField("WLAN", max_length=200, blank=True)
    bluetooth = models.CharField("Bluetooth", max_length=200, blank=True)
    gps = models.CharField("GPS", max_length=200, blank=True)
    nfc = models.CharField("NFC", max_length=200, blank=True)
    radio = models.CharField("Radio", max_length=200, blank=True)
    usb = models.CharField("USB", max_length=200, blank=True)
    
    features = models.CharField("FEATURES", max_length=200, default='FEATURES') # FEATURES
    Sensors = models.CharField("Sensors", max_length=200, blank=True)

    battery = models.CharField("BATTERY", max_length=200, default='BATTERY') # BATTERY
    type = models.CharField("Type", max_length=200, blank=True)
    charging = models.TextField("Charging", max_length=200, blank=True)

    misc = models.CharField("MISC", max_length=200, default='MISC') # MISC
    colors = models.CharField("Colors", max_length=200, blank=True)
    modelss = models.CharField("Models", max_length=200, blank=True)
    sar = models.CharField("SAR", max_length=200, blank=True)
    sarEu = models.CharField("SAR EU", max_length=200, blank=True)
    price = models.CharField("Price", max_length=200, blank=True)

    tests = models.CharField("TESTS", max_length=200, default='TESTS') # TESTS
    performance = models.TextField("Performance", max_length=200, blank=True)
    displayTest = models.CharField("Display Test", max_length=200, blank=True)
    camera = models.CharField("Camera", max_length=200, blank=True)
    loudspeaker = models.CharField("Loudspeaker", max_length=200, blank=True)
    battery_life = models.CharField("Battery life", max_length=200, blank=True)

    def __str__(self):
        return str(self.name)




