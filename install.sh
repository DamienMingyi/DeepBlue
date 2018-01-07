# install log4cplus

# install rfoo
git clone https://github.com/aaiyer/rfoo.git
cd rfoo; python setup.py install

# install other python dependence
pip install pid
pip install supervisor   # (use python2.7 pip)

# change python path in ./rpm/install.sh, then:
./rpm/install.sh

# change run user name and supervisor command path in /usr/local/ete/*
# edit /etc/ld.so.conf.d/ctp.conf
# edit /usr/local/etc/kungfu/kungfu.json