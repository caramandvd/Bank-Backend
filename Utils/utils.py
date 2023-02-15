from sqlalchemy import create_engine, text

from Model.Domain.USER import User

engine = create_engine('mysql+pymysql://root:@localhost:3306/bankdashboarddb', echo=True)



if __name__ == '__main__':
    all_users = []
    with engine.connect() as conn:
        query = conn.execute (text("SELECT * FROM users"))
        for user in query:
            user = User(
                user_id=user[0],
                first_name=user[1],
                last_name=user[2],
                email_name=user[3],
                address=user[4],
                phone_number=user[5],
                date_of_birth=user[6],
                join_date=user[7]
            )
            all_users.append(user)
    print(all_users)

    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM users'))
        for user in query:
            print(user)