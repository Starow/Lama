LAMA-WORDLIST
===========
Downloads directory: http://


Compiling
---------
To compile for Linux


If you want do download the development tree with git, be sure to do a *complete* checkout with `--recursive` and then run `bootstrap.sh`, `configure` and `make`:

    git clone --recursive https://github.com/Starow/Lama
    cd tcpflow
    sh bootstrap.sh
    ./configure
    make
    sudo make install  

To download and compile for Amazon AMI:

	ssh ec2-user@<your ec2 instance>
	sudo bash yum -y install git make gcc-c++ automake autoconf boost-devel cairo-devel libpcap-devel zlib-devel
	git clone --recursive https://github.com/simsong/tcpflow.git
	sh bootstrap.sh


Introduction To Lama-Wordlist
=======================

Description du Projet:
Création de word-list comprennant des informations de réseaux sociaux.

3 parties distincts:
==> Récupération d'informations brutes sur les réseaux sociaux.
	Via API Facebook, Graph, Twitter etc.

==> Création d'une liste de mots dans un format adapté.
	Format à définir.

==> Génération de word-lists comprennant les permutations nécéssaires.