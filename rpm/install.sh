sudo cp -r ./* /usr/local/
sudo mkdir -p /opt/kungfu/log

sudo cat > /etc/ld.so.conf.d/ctp.conf <<EOF
/usr/local/lib/yijinjing/
/usr/local/lib/wingchun/
EOF