from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>欢迎使用维006的ip代理池</h2>\n<h4>输入“http://localhost:5200/random”将随机弹出一个可用ip</h4>'


@app.route('/random')
def get_proxy():
    """
    获取一个随机代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    获得代理池所有代理
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


@app.route('/use')
def get_all():
    """
    获取所有满分代理
    :return: 所有可用代理
    """
    conn = get_conn()
    return conn.use()


if __name__ == '__main__':
    app.run()
