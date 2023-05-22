import sys
sys.path.insert(0, '../voice_tools')
import time

from transformers import AutoTokenizer, AutoModel, pipeline
from textToSpeech import textToSpeech

def questionAnswer(question):
    start = time.time()
    print("===========")
    question_answerer = pipeline(
        "question-answering",
        model="Rifky/Indobert-QA",
        tokenizer="Rifky/Indobert-QA"
    )

    context = "Selamat datang di apartemen kami, kami memiliki beberapa jenis tipe apartemen, ada tipe studio luxury, studio X12, studio diamond. Kami saat ini sedang memiliki promo untuk apartemen tipe X12 yaitu dengan harga 1,25M rupiah. Tipe apartemen kami ada X12, X15, X17 dan X19."

    context2 = """Secara historis konflik di Sudan terjadi akibat ketegangan etnis, perselisihan agama, dan persaingan memperebutkan sumber daya.[9][10] Penggunaan tanah dan air telah menjadi pendorong utama konflik, khususnya antara petani menetap dan penggembala nomaden,[11] dengan pertanian menjadi sektor penting dalam perekonomian Sudan.[12] Dua perang saudara antara pemerintah pusat dan wilayah selatan menewaskan 1,5 juta orang, dan konflik berkelanjutan di wilayah barat Darfur telah mendorong dua juta orang meninggalkan rumah mereka dan menewaskan lebih dari 200.000 orang.[13] Sejak kemerdekaan pada tahun 1956, Sudan telah mengalami lebih dari lima belas kudeta militer[14] dan telah diperintah oleh militer untuk sebagian besar wilayah republik dan pernah secara singkat oleh pemerintahan parlementer sipil yang demokratis.[15]

    Konteks politik
    Mantan presiden dan orang berpengaruh dalam militer, Omar al-Bashir, memimpin perang di bagian barat negara itu dan mengawasi kekerasan yang disponsori negara di wilayah Darfur, yang menyebabkan tuduhan kejahatan perang dan genosida.[16] Tokoh kunci dalam konflik Darfur termasuk Mohamed Hamdan "Hemedti" Dagalo, komandan Pasukan Pendukung Cepat pada saat bentrokan tahun 2023.[5] Pada tahun 2019, kudeta menggulingkan al-Bashir dalam konteks pembangkangan sipil besar-besaran yang sering digambarkan sebagai tahap pertama Revolusi Sudan. Pemerintah persatuan sipil-militer gabungan sementara yang dipimpin oleh Perdana Menteri Abdallah Hamdok didirikan.[16] Namun, pada Oktober 2021, militer merebut kekuasaan melalui kudeta yang dipimpin oleh pemimpin Angkatan Bersenjata Sudan Abdel Fattah al-Burhan dan pemimpin RSF Dagalo. Al-Burhan menjadi pemimpin junta yang efektif, memonopoli kekuasaan.[17]

    Junta kemudian setuju untuk menyerahkan kekuasaan kepada pemerintah yang dipimpin sipil, dengan kesepakatan resmi yang dijadwalkan akan ditandatangani pada 6 April 2023.[18] Namun, itu tertunda karena ketegangan antara jenderal Burhan dan Dagalo, yang masing-masing menjabat sebagai ketua dan wakil ketua Dewan Kedaulatan Transisi.[19] Di antara perselisihan politik mereka adalah integrasi RSF ke dalam militer.[20] Salah satu masalah yang diperdebatkan itu ialah desakan RSF untuk diintegrasikan ke tentara reguler dalam waktu sepuluh tahun, sedangkan tentara reguler menuntut hal itu dilakukan dalam dua tahun.[5] Isu lain yang diperdebatkan termasuk status yang diberikan kepada perwira RSF dalam hirarki masa depan, dan apakah pasukan RSF harus berada di bawah komando panglima angkatan darat – bukannya panglima tertinggi Sudan – yang saat ini adalah Burhan.[21] Sebagai tanda keretakan mereka, Dagalo menyatakan penyesalan atas kudeta Oktober 2021.[17]

    Pasukan Dukungan Cepat
    RSF adalah organisasi paramiliter yang berakar pada milisi Janjaweed yang beroperasi selama Perang Darfur.[22] Itu secara resmi dibuat oleh Presiden Bashir pada tahun 2013 dan dipimpin oleh Dagalo dan diawasi langsung oleh Bashir.[23] Mereka menjadi terkenal karena menindak pengunjuk rasa pro-demokrasi selama pembantaian Khartoum pada Juni 2019.[22] Rezim Bashir mengizinkan beberapa kelompok bersenjata, termasuk RSF, untuk berkembang guna mencegah ancaman terhadap keamanannya dari dalam angkatan bersenjata, sebuah praktik yang dikenal sebagai "pembuktian kudeta".[24] Baik RSF dan tentara mendapat manfaat dari pelatihan keamanan dan pengiriman senjata dari Rusia dengan imbalan emas.[25] Konsolidasi kekuasaan RSF dan Dagalo berjalan seiring dengan akumulasi kekayaan yang cepat, dengan kepala paramiliter merebut lokasi penambangan emas utama di Darfur dan mengintervensi atas nama pasukan koalisi pimpinan Saudi selama Perang Saudara Yaman dan berkolusi dengan Grup Wagner untuk mendanai upaya perang Rusia di Ukraina melalui penyelundupan emas. Hal ini menyebabkan pasukan RSF berkembang pesat menjadi puluhan ribu, termasuk ribuan truk pikap bersenjata, yang secara rutin berpatroli di jalan-jalan Khartoum.[23] Sudan secara konsisten membantah kehadiran Wagner di wilayahnya.[26][27]

    Manuver awal
    Pada 11 April 2023, pasukan RSF dikerahkan di dekat kota Merowe dan di Khartoum. Pasukan pemerintah memerintahkan mereka untuk pergi, tetapi mereka menolak, menyebabkan bentrokan ketika pasukan RSF menguasai pangkalan militer Soba di selatan Khartoum.[28] Pasukan Dukungan Cepat memulai mobilisasi mereka pada 13 April 2023, menimbulkan kekhawatiran akan pemberontakan melawan junta. Angkatan Bersenjata Sudan mengatakan mobilisasi itu ilegal.[29]"""

    question2 = "Kapan perang sudah dimulai?"
    preds = question_answerer(question=question, context=context)


    print(
        f"answer: {preds['answer']}\nscore: {round(preds['score'], 4)}\nstart: {preds['start']}\nend: {preds['end']}"
    )

    print("Time to process : ", time.time() - start)
    print("===========")
    return f"{preds['answer']}"


