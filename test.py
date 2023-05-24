

'''
<!-- Ajouter une image -->
<img src="chemin/vers/image.png" alt="Description de l'image">

<!-- Ajouter un paragraphe de texte -->
<p>Ceci est un paragraphe de texte.</p>

<!-- Ajouter une vidéo -->
<video width="320" height="240" controls>
  <source src="chemin/vers/video.mp4" type="video/mp4">
  <source src="chemin/vers/video.ogg" type="video/ogg">
  Votre navigateur ne supporte pas la lecture de vidéos.
</video> '''

header {
    background-color: #000; /* couleur de fond de la barre de navigation */
    height: 150px; /* hauteur de la barre de navigation */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 50px; /* espacement entre le logo et la barre de navigation */
}


nav ul {
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
}
  
nav li {
    margin: 0 10px;
}
  
nav a {
    display: block;
    padding: 10px;
    color: #fff; /* couleur du texte des boutons de navigation */
    text-decoration: none;
    font-size: 20px; /* taille de police des boutons de navigation */
}
  
img {
    height: 60px; /* hauteur de votre logo */
}


<img src="/Applications/MAMP/htdocs/Git_server/site-la-plateforme/Annexe/noir_et_blanc.jpeg" alt="Logo de mon site">


header {
    background-image: url('/Applications/MAMP/htdocs/Git_server/site-la-plateforme/Annexe/x.jp2');
    background-repeat: no-repeat;   /* pour éviter que l'image se répète */
    background-size: cover;         /* pour couvrir toute la largeur et hauteur de l'en-tête */
    height: 150px;                  /* hauteur de la barre de navigation */
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 50px;                /* espacement entre le logo et la barre de navigation */
}

@media screen and (max-width:900px) {
    a {
        font-size: 0.6rem;
    }
    
}
img {
    width: 100vw;
}

header {
    background-image: url('');
    background-repeat: no-repeat;   /* pour éviter que l'image se répète */
    background-size: cover;         /* pour couvrir toute la largeur et hauteur de l'en-tête */
    height: 150px;                  /* hauteur de la barre de navigation */
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 50px;                 /* espacement entre les bords de l'en-tête et les éléments qu'il contient */
}

nav ul {
    display: flex;
    justify-content: center;        /* pour centrer horizontalement */
    align-items: center;            /* pour centrer verticalement */
}
  
li {
    display: inline-block;
    margin: 0 10px;
}

a {
    text-decoration: none;
    color: #333;
    font-size: 18px;
    font-weight: bold;
}

body {
    background-image: url('Annexe/x.jp2');
    background-size: cover;
    background-repeat: no-repeat;
}
