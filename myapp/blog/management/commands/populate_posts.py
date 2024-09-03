from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data 
        Post.objects.all().delete()

        titles = [
            "Helmet Detection and Face Recognition",
            "Ancient Tamil Script Recognition using Machine Learning",
            "File Sharing Application",
            "Calculator Application",
            "User Management System using Flask and MySQL Database",
            "White Board Application using Python Tkinter",
            "Delhi Diaries",
            "Kodaikanal The Queen of Hills",
            "Bhopal: Gaining Technical Insights",
            "Pondicherry",
            "Chennai: Lessons from a Life-Changing City",
            "Freefire: 700K YouTube Journey",
            "FIFA",
            "GTA5",
            "Cricket",
            "Football",
            "Biriyani",
            "Gold Prawn",
            "Rasmalai",
            "Blueberry Cocktail",
        ]

        contents = [
            "Detail the process of integrating Yolo algorithm and Flask to create a system for detecting helmets and recognizing faces in workplace environments. Discuss technical challenges overcome and the functionalities achieved.",
            "Explain the steps taken to train a TensorFlow model for recognizing ancient Tamil script characters. Discuss the cultural significance of preserving heritage through technology and the results achieved.",
            "Walk through the development of a file sharing application with features like file selection, uploading, downloading, and considerations for user interface design using Tkinter.",
            "Provide a tutorial on creating a basic calculator application in Python, covering arithmetic operations, user input handling, and if applicable, GUI implementation with Tkinter.",
            "Outline the design and implementation of a user management system with features like authentication, CRUD operations on user data, and considerations for security using Flask and MySQL.",
            "Describe the development of a digital whiteboard application using Tkinter, highlighting features such as drawing tools, color selection, and saving drawings on the user interface.",
            "Dive into my journey through Delhi in 2020, where I explored iconic landmarks like the Red Fort and Taj Mahal. From navigating the bustling streets to savoring local street food in Chandni Chowk, every moment was a blend of cultural immersion and historical discovery.",
            "Discover why Kodaikanal holds a special place in my heart as the Queen of Hills. From tranquil boat rides on the lake to breathtaking views from Coaker's Walk, I'll share insider tips and personal stories that capture the essence of this picturesque getaway.",
            "My Internship in Bhopal from December 2023 to March 2024, discussing the technical skills acquired and insights into the business environment. Share experiences exploring the city's lakes, visiting malls, parks, and interacting with locals. Describe cultural encounters such as attending festivals or experiencing traditional cuisine, highlighting how these experiences enriched your professional and personal growth.",
            "Experience the charm of Pondicherry through my eyes, where days were spent soaking in the sun on Paradise Beach and evenings enjoying the lively atmosphere of its pubs. From exploring French colonial architecture to indulging in delicious fusion cuisine, Pondicherry offered a perfect blend of relaxation and adventure.",
            "Chennai, where I pursued my UG Degree studies, taught me invaluable lessons in independence and resilience. From navigating academic challenges to forging lifelong friendships, every experience in this dynamic city shaped my personal and professional journey.",
            "As an E-Sport player of Freefire, I've built a YouTube channel with 700K subscribers and received the Silver Play Button—a truly unforgettable milestone in my gaming journey.",
            "FIFA holds a special place in my heart as the ultimate football game, with Ronaldo as my favorite player. Explore my love for the sport and the exhilarating gameplay of FIFA.",
            "GTA5 has been my favorite game since childhood, offering endless excitement and exploration. Discover why this game remains a cherished part of my gaming journey.",
            "Cricket isn't just a game; it's an emotional journey for me. Explore my admiration for MS Dhoni and my love for the Chennai Super Kings.",
            "Football has always been my childhood dream, fueled by my admiration for Ronaldo. Discover my journey on the field and my passion for the beautiful game.",
            "Biryani is not just a dish but a passion, especially when it's the iconic Dindigul Thalappakatti Biryani from my native. Join me as I delve into the flavors and history of this beloved dish.",
            "Gold Prawn is my ultimate seafood indulgence, cherished for its exquisite taste and unique flavors. Discover why this dish holds a special place in my culinary adventures.",
            "Rasmalai is more than just a dessert; it's a nostalgic treat that brings back fond memories. Join me in savoring the creamy richness and delicate sweetness of this beloved sweet.",
            "Blueberry Cocktail is my go-to refreshment, offering a burst of fruity flavors and a refreshing experience. Dive into the vibrant blend of flavors that make this cocktail a favorite choice.",
        ]

        img_urls = [
            "https://dfzljdn9uc3pi.cloudfront.net/2020/cs-311/1/fig-2-full.png",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF4zBUB0nh8mvHkwnslzA2fEcfyyUPmdEpnQ&s",
            "https://windowsreport.com/wp-content/uploads/2020/03/best-file-sharing-software-and-tools.jpg",
            "https://i.ytimg.com/vi/6CZB6VTy3Hg/hqdefault.jpg",
            "https://abhyastprojects.com/wp-content/uploads/2024/02/product_image.png",
            "https://conceptboard.com/wp-content/uploads/CCB-header-whiteboarding-2-e1585068868879.png",
            "https://im.whatshot.in/img/2020/Jul/fb-1593758772.jpg",
            "https://img.traveltriangle.com/blog/wp-content/uploads/2023/07/Kodaikanal.jpg?tr=w-400",
            "https://upload.wikimedia.org/wikipedia/commons/0/08/Bhopal_lake_view.jpg",
            "https://www.oyorooms.com/travel-guide/wp-content/uploads/2021/08/GlobalBannerRevamp-Blog3-1-1280x720.jpg",
            "https://www.abhibus.com/blog/wp-content/uploads/2023/10/Things-to-Do-in-Chennai-for-Every-Traveler.jpg",
            "https://w0.peakpx.com/wallpaper/969/413/HD-wallpaper-garena-fire-poster-2019-games-mobile-games-gff.jpg",
            "https://i.guim.co.uk/img/media/4cd2e3dfef9da0adb8f4ea1294d4d1097f50bd63/152_0_2234_1342/master/2234.jpg?width=1200&quality=85&auto=format&fit=max&s=e556f1df87e5634ae249d37073a327e1",
            "https://static.independent.co.uk/s3fs-public/thumbnails/image/2013/10/07/14/original.jpg",
            "https://images.indianexpress.com/2023/05/Dhoni.jpg",
            "https://img.bleacherreport.net/img/images/photos/003/222/202/71527029afbb7d341c57269ee3fbde26_crop_north.jpg?1420463327&w=3072&h=2048",
            "https://m.media-amazon.com/images/I/51AcdwPj-YL._AC_UF1000,1000_QL80_.jpg",
            "https://therecipecritic.com/wp-content/uploads/2020/01/broiled_lobster2.jpg",
            "https://www.kashmironlinestore.com/cdn/shop/articles/Untitled_design_54_1024x.jpg?v=1692702218",
            "https://ik.imagekit.io/vjt1kualr/drinks/blueberry_martini/main-image.jpg",
        ]
        
        categories = Category.objects.all()
        for title, content, img_url in zip(titles, contents, img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))