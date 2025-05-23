import random
from contacts.models import Contact
from leads.models import Lead
from deals.models import Deal
from tasks.models import Task
from django.contrib.auth.models import User
from django.utils import timezone

user = User.objects.first()
if not user:
    raise Exception("Avval User yarating! (python manage.py createsuperuser)")

# Yordamchi ma'lumotlar
first_names = [
    "Azizbek", "Dilnoza", "Shaxzod", "Madina", "Sardor", "Gulnoza", "Islom", "Zarina", "Jasur", "Nodira",
    "Otabek", "Malika", "Botir", "Shoira", "Sherzod", "Rano", "Bekzod", "Lola", "Iroda", "Ulug‘bek",
    "Farrux", "Nilufar", "Temur", "Dilorom", "Komil", "Sabina", "Akmal", "Rayhon", "Samandar", "Gulbahor"
]
last_names = [
    "Rahimov", "Ismoilova", "Yuldashev", "Toirova", "Qurbonov", "Karimova", "Usmonov", "Abdullayeva", "Xudoyberdiyev", "Turg‘unova",
    "Qodirov", "Normatova", "Iskandarov", "Solieva", "Bekchanov", "Pulatova", "G‘ofurov", "Odilova", "Sharipov", "Olimova",
    "Valiyev", "Juraeva", "Davlatov", "Sobirova", "Sodiqov", "Mirzayeva", "Nazarov", "Qo‘chqarova", "Jabborov", "Tojiboyeva"
]
companies = [
    "Toshkent Fashion", "SamStyle", "ModaBiz", "ElegantLine", "UstozStyle", "YangiUslub", "GrandDress", "Barchinoy Moda", "FitLife Wear", "TillaKiyim",
    "Avangard", "Shahzoda Style", "Zarifcha", "TopTrend", "RoyalWear", "FashionCity", "ModaMarkaz", "Klassika", "UzTrend", "Zarafshan Kiyim",
    "CityLook", "DressHub", "Asal Moda", "Raqamli Moda", "Glamour", "StyleMix", "UltraFashion", "SimSim", "HayotStyle", "BahorModa"
]
positions = [
    "Do‘kon egasi", "Bozor sotuvchisi", "Marketing menejeri", "Sotuvchi", "Direktor", "Boshqaruvchi", "Savdo agenti", "Menecer", "Hududiy menejer", "Sotib oluvchi"
]
addresses = [
    "Toshkent shahri, Chilonzor tumani", "Samarqand, Siab bozori", "Andijon, Asaka tumani", "Namangan, Chorsu bozori", "Nukus, Amudaryo ko‘chasi",
    "Farg‘ona, Markaziy bozor", "Buxoro, Mustaqillik ko‘chasi", "Qarshi, Do‘stlik mahallasi", "Jizzax, Sharq ko‘chasi", "Qo‘qon, Istiqlol ko‘chasi"
]

lead_titles = [
    "Yozgi kolleksiya uchun buyurtma", "Qishki palto importi", "Bolalar sport kostyumlari", "Ofis kiyimlari", "Maktab formasi buyurtmasi",
    "Yirik ulgurji buyurtma", "Ayollar bahorgi liboslari", "Erkaklar to‘plami", "Onalar uchun yangi kolleksiya", "Yoshlar streetwear",
    "Sochiq va uy tovarlari", "Kiyim aksessuarlari", "Brend katalogi buyurtmasi", "Sport kiyimlar", "Xalatlar va pijamalar",
    "Asosiy yetkazib berish", "Namuna olish", "Sinov partiyasi", "Maxsus dizayn", "Chegirma aksiyasi",
    "Yangi hamkorlik", "Ommaviy savdo", "Rasmiy tender", "Maxfiy buyurtma", "Individual buyurtma",
    "Eksport shartnomasi", "Mahalliy distribyutor", "Yillik shartnoma", "Yozgi aksiya", "Chegirma haftaligi"
]

lead_desc = [
    "Kiyim-kechak kolleksiyasi uchun narx va assortiment so‘radi.",
    "Yirik buyurtmaga qiziqish bildirdi.",
    "Yangi kolleksiyani ko‘rishni xohlaydi.",
    "Tijorat taklifi talab qilindi.",
    "Hamkorlik shartlari bo‘yicha savol berdi.",
    "Narxlar va yetkazib berish haqida ma’lumot so‘radi.",
    "Ofis uchun maxsus kiyimlar kerak.",
    "Bolalar uchun sport to‘plami qiziqtirdi.",
    "Yangi yetkazib beruvchi kerakligini bildirdi.",
    "Brend katalogiga buyurtma bermoqchi."
]

# Telefon raqamidan +998 ni olib tashlaymiz
def clean_phone(phone):
    if phone.startswith('+998'):
        return phone[4:]
    elif phone.startswith('998'):
        return phone[3:]
    return phone

contacts = []
leads = []
deals = []
tasks = []

for i in range(30):
    first = first_names[i]
    last = last_names[i]
    company = companies[i]
    position = random.choice(positions)
    address = random.choice(addresses)
    email = f"{first.lower()}.{last.lower()}@{company.lower().replace(' ', '')}.uz"
    phone = clean_phone(f"+998{random.randint(900000000, 999999999)}")
    contact = Contact.objects.create(
        first_name=first,
        last_name=last,
        email=email,
        phone=phone,
        company=company,
        position=position,
        address=address,
        source=random.choice(['website', 'referral', 'social_media', 'email', 'other']),
        notes=random.choice(["Eng yirik mijoz", "Potensial yangi mijoz", "Hamkorlik bo‘yicha muzokara", "Doimiy buyurtmachi", ""]),
        assigned_to=user,
        created_by=user
    )
    contacts.append(contact)

    lead = Lead.objects.create(
        contact=contact,
        title=lead_titles[i],
        status=random.choice(['new', 'contacted', 'qualified', 'unqualified', 'converted']),
        priority=random.choice(['low', 'medium', 'high']),
        description=random.choice(lead_desc),
        estimated_value=random.randint(5000, 90000),
        assigned_to=user,
        created_by=user
    )
    leads.append(lead)

    deal = Deal.objects.create(
        title=f"{lead_titles[i]} bitimi",
        contact=contact,
        lead=lead,
        stage=random.choice(['discovery', 'proposal', 'negotiation', 'closed_won', 'closed_lost']),
        amount=random.randint(4000, 80000),
        expected_close_date=timezone.now().date() + timezone.timedelta(days=random.randint(5, 60)),
        probability=random.choice([40, 50, 60, 70, 80, 90]),
        description=lead_desc[i % len(lead_desc)],
        assigned_to=user,
        created_by=user
    )
    deals.append(deal)

    task = Task.objects.create(
        title=f"{lead_titles[i]} vazifasi",
        description=f"{lead_titles[i]} uchun vazifa bajarilishi kerak.",
        status=random.choice(['not_started', 'in_progress', 'completed', 'deferred']),
        priority=random.choice(['low', 'medium', 'high']),
        due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
        contact=contact,
        lead=lead,
        deal=deal,
        assigned_to=user,
        created_by=user
    )
    tasks.append(task)

print("Bazaga 30 ta contact, lead, deal va task muvaffaqiyatli qo'shildi!")
