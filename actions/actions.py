# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from transformers import pipeline

qa_pipeline = pipeline(
    task="question-answering",
    model="Rifky/Indobert-QA",
    tokenizer="Rifky/Indobert-QA"
)

class ActionHelloRoom(Action):
    def name(self) -> Text:
         return "action_hello_room"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.get_slot("unit_type")

        if user_input == "studio":
            dispatcher.utter_message(text="Hey! selamat datang ke ****** untuk melihat kelas apartemen studio, perkenalkan kembali saya adalah asisten virtualmu untuk menemanimu selama disini.")
        elif user_input == "satu kamar":
            dispatcher.utter_message(text="Hey! selamat datang ke ****** untuk melihat kelas apartemen 1 kamar, perkenalkan kembali saya adalah asisten virtualmu untuk menemanimu selama disini.")
        elif user_input == "dua kamar":
            dispatcher.utter_message(text="Hey! selamat datang ke ****** untuk melihat kelas apartemen dua kamar, perkenalkan kembali saya adalah asisten virtualmu untuk menemanimu selama disini.")
        
        return []

class ActionApartmentKnowledge(Action):
    def name(self) -> Text:
        return "action_apartmentKnowledge"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.get_slot("unit_type")
        user_question = tracker.get_slot("user_question")

        if user_input == "studio":
            result = qa_pipeline({
                'context': """Selamat datang di apartemen studio kami yang modern dan nyaman! Terletak di pusat kota yang sibuk, apartemen ini merupakan pilihan sempurna untuk individu atau pasangan yang ingin tinggal dalam lingkungan yang hidup dan dinamis.
                Apartemen studio ini menawarkan ruang terbuka yang luas dan cerah dengan desain yang sangat terorganisir. Ruang tamu yang nyaman dan kamar tidur terintegrasi menciptakan lingkungan yang efisien dan fungsional. Dinding putih bersih dan lantai kayu yang indah memberikan sentuhan elegan pada interior apartemen.
                Dapur kecil namun lengkap dilengkapi dengan peralatan modern seperti kompor induksi, oven microwave, dan lemari es. Anda dapat dengan mudah memasak hidangan favorit Anda tanpa harus meninggalkan kenyamanan apartemen. Ada juga meja makan kecil di samping dapur untuk menikmati hidangan Anda.
                Kamar mandi yang elegan dilengkapi dengan shower dan perlengkapan mandi yang lengkap, menciptakan suasana santai di mana Anda dapat merawat diri setelah hari yang panjang.
                Dengan adanya jendela besar, apartemen ini dibanjiri sinar matahari alami, memberikan tampilan indah ke luar dan memberikan suasana ceria di dalam. Untuk kenyamanan Anda, apartemen ini juga dilengkapi dengan pendingin udara dan pemanas untuk menghadapi segala perubahan cuaca. 
                Selain interior yang menawan, apartemen ini juga memiliki fasilitas yang luar biasa. Pusat kebugaran modern dan kolam renang yang menyegarkan siap untuk digunakan kapan saja. Ada juga ruang serbaguna yang dapat digunakan untuk pertemuan atau acara sosial.
                Terletak hanya beberapa langkah dari pusat perbelanjaan, restoran, dan tempat hiburan terkenal, apartemen ini menawarkan akses yang mudah ke semua yang kota ini tawarkan. Stasiun transportasi publik juga dekat, memudahkan Anda dalam menjelajahi kota ini tanpa kesulitan.
                Dengan biaya sewa yang terjangkau dan fasilitas yang lengkap, apartemen studio ini adalah pilihan ideal bagi mereka yang menginginkan gaya hidup perkotaan yang nyaman. Jangan lewatkan kesempatan ini, segera hubungi kami untuk mengatur jadwal kunjungan dan rasakan kenyamanannya sendiri""",
                'question': f"{user_question}"
            })
            dispatcher.utter_message(text=result)

        elif user_input == "satu kamar":
            result = qa_pipeline({
                'context': """Selamat datang di apartemen satu kamar tidur yang modern dan nyaman ini! Terletak di lingkungan yang ramai, apartemen ini merupakan pilihan ideal untuk individu atau pasangan yang menginginkan ruang pribadi yang fungsional dan bergaya.
                Apartemen ini menawarkan interior yang terorganisir dengan baik, menciptakan ruang hidup yang efisien dan menyenangkan. Ruang tamu terbuka dan cerah menyambut Anda begitu memasuki apartemen. Dengan dinding netral yang bersih dan lantai kayu yang indah, apartemen ini memberikan tampilan yang segar dan modern.
                Dapur kecil namun lengkap dilengkapi dengan peralatan modern seperti kompor listrik, oven microwave, dan lemari es. Anda dapat dengan mudah memasak hidangan favorit Anda tanpa kesulitan. Ada juga area makan yang nyaman di sebelah dapur, tempat Anda dapat menikmati hidangan dengan kenyamanan.
                Kamar tidur utama yang luas menawarkan tempat tidur yang nyaman dan lemari besar untuk menyimpan pakaian Anda. Dengan jendela yang besar, kamar tidur ini dibanjiri cahaya alami, menciptakan suasana yang hangat dan menyegarkan.
                Kamar mandi modern dilengkapi dengan shower dan perlengkapan mandi yang lengkap, memastikan kenyamanan dan kebersihan Anda setiap hari.
                Apartemen ini juga dilengkapi dengan fasilitas tambahan yang menarik. Terdapat ruang penyimpanan ekstra di dalam apartemen untuk memenuhi kebutuhan Anda akan ruang. Selain itu, terdapat pusat kebugaran yang lengkap dengan peralatan modern dan ruang komunitas yang dapat digunakan untuk pertemuan atau acara sosial.
                Lokasinya yang strategis membuat apartemen ini menjadi tempat yang sempurna untuk menjalani gaya hidup perkotaan. Terdapat berbagai pusat perbelanjaan, restoran, dan tempat hiburan terkenal yang dapat Anda jangkau dengan mudah. Akses ke transportasi publik juga sangat nyaman, memungkinkan Anda untuk menjelajahi kota dengan mudah.
                Apartemen satu kamar ini menawarkan keseimbangan yang sempurna antara kenyamanan dan gaya hidup perkotaan yang dinamis. Jangan lewatkan kesempatan ini, hubungi kami sekarang untuk mengatur jadwal kunjungan dan melihat keindahan apartemen ini secara langsung!""",
                'question': f"{user_question}"
            })
            dispatcher.utter_message(text=result)

        elif user_input == "dua kamar":
            result = qa_pipeline({
                'context': """Selamat datang di apartemen dua kamar tidur yang elegan dan modern ini! Terletak di lingkungan yang bergengsi, apartemen ini menawarkan pengalaman hunian yang mewah dan nyaman bagi keluarga atau pasangan yang membutuhkan ruang ekstra.
                Apartemen ini menampilkan interior yang luas dan terang, dirancang dengan sentuhan kontemporer yang menawan. Ruang tamu yang luas menawarkan tempat yang sempurna untuk bersantai dan menghibur tamu Anda. Dengan lantai kayu indah dan dinding netral yang dilengkapi dengan aksen dekoratif yang menarik, apartemen ini menciptakan suasana yang hangat dan mengundang.
                Dapur yang modern dan lengkap dengan peralatan terbaru adalah impian para pecinta masak. Dengan lemari dapur yang elegan, meja kerja yang luas, kompor gas, oven, dan lemari es berkapasitas besar, Anda akan memiliki semua yang Anda butuhkan untuk mempersiapkan hidangan lezat. Ada juga sebuah meja makan yang nyaman di dekatnya, sehingga Anda dapat menikmati makanan dengan keluarga atau teman-teman dengan mudah.
                Kedua kamar tidur yang luas menawarkan kenyamanan dan privasi. Kamar tidur utama menampilkan tempat tidur yang nyaman dan lemari besar untuk menyimpan pakaian Anda. Kamar tidur kedua juga cukup luas dan dapat diubah menjadi ruang kerja atau ruang main anak-anak, sesuai dengan kebutuhan Anda. Kedua kamar tidur dilengkapi dengan jendela besar yang memberikan pemandangan yang indah dan memastikan pencahayaan alami yang melimpah.
                Dua kamar mandi yang mewah menghadirkan kenyamanan ekstra bagi penghuni apartemen. Kamar mandi utama dilengkapi dengan bathtub yang nyaman dan shower terpisah, sedangkan kamar mandi kedua memiliki shower. Keduanya dilengkapi dengan perlengkapan mandi berkualitas tinggi untuk memberikan pengalaman relaksasi yang optimal.
                Selain interior yang mengesankan, apartemen ini juga menawarkan fasilitas kelas atas. Terdapat pusat kebugaran modern yang dilengkapi dengan peralatan terbaru dan kolam renang infinity yang menakjubkan, tempat Anda dapat berolahraga dan bersantai. Ada juga ruang komunitas yang luas yang bisa digunakan untuk pertemuan atau acara bersama.
                Apartemen ini terletak di lingkungan yang premium, dengan akses mudah ke pusat perbelanjaan, restoran, taman, dan tempat hiburan. Stasiun transportasi publik juga berada dalam jarak yang mudah dijangkau, memudahkan perjalanan Anda di dalam dan sekitar kota.
                Apartment dengan dua kamar tidur ini adalah pilihan sempurna bagi mereka yang mencari hunian yang elegan dan modern dengan ruang ekstra. Jangan lewatkan kesempatan ini, segera hubungi kami sekarang untuk mengatur jadwal kunjungan dan rasakan kenyamanan serta keindahan apartemen ini sendiri!""",
                'question': f"{user_question}"
            })
            dispatcher.utter_message(text=result)

            return []

