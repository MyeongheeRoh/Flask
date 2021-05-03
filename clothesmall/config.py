class ClothesmallConfig(object):
    #: 데이터베이스 연결 URL
    DB_URL= 'postgresql://mae:mae1234@localhost:5432/postgres'
    #: 데이터베이스 파일 경로
    DB_FILE_PATH= 'resource/database'
    #: 로그 레벨 설정
    LOG_LEVEL = 'debug'
    #: 디폴트 SQLAlchemy trace log 설정
    DB_LOG_FLAG = 'True'