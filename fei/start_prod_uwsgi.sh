set -e source /root/setup_env.sh
uwsgi prod_docker.ini --static-map /static=/usr/src/app/collect_serve
