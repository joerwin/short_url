from app.database.impl.ShortUrlDaoSqlLiteImpl import ShortUrlDaoSqlLiteImpl

if __name__ == '__main__':
    print 'Installing tables...'
    ShortUrlDaoSqlLiteImpl().install_tables()
    print 'Done.'
