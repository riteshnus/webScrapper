from sqlalchemy.orm import sessionmaker
from models import Cyclones, db_connect, create_cyclone_table

class CyclonePipeline(object):
    """Cyclones pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates cyclone table.
        """
        engine = db_connect()
        create_cyclone_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        cyclone = Cyclones(**item)

        try:
            session.add(cyclone)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item