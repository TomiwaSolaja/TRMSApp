from sqlite3 import Cursor
from Repos.request_repo import Requestrepo
from models.request import Request
from util.db_connection import connection

class RequestRepoImpl(Requestrepo):
    def create_request(self, request):
        sql="INSERT INTO requests VALUES (%s, %s,%s, %s,%s, %s,%s, %s, %s) RETURNING *"
        cursor= connection.cursor()
        cursor.execute(sql,[request.req_id, request.req_type, request.cost, request.amount, request.grade, request.status, request.event_date, request.location, request.emp_id])
        connection.commit()
        record=cursor.fetchone()
        return Request(req_id=record[0], req_type=record[1], cost=record[2], amount=record[3], grade=record[4],status=record[5], event_date=record[6], location=record[7], emp_id=record[8])
    
    def get_request(self, req_id):
        sql = "SELECT * FROM requests WHERE req_id= %s"
        cursor= connection.cursor()
        cursor.execute(sql, [req_id])
        record= cursor.fetchone()
        if record:
            return Request(req_id=record[0], req_type=record[1], cost=record[2], amount=record[3], grade=record[4],status=record[5], event_date=record[6], location=record[7], emp_id=record[8])
        else:
            raise print(f"client id not found {req_id}")
        return
    
    def all_requests(self, emp_id):
        sql= "SELECT * FROM requests WHERE emp_id=%s"
        cursor= connection.cursor()
        cursor.execute(sql,[emp_id])
        records=cursor.fetchall()
        requests=[]
        for record in records:
            request= Request(req_id=record[0], req_type=record[1], cost=record[2], amount=record[3], grade=record[4],status=record[5], event_date=record[6], location=record[7], emp_id=record[8])
            requests.append(request)
        return requests
    
    def update_request(self, change):
        return super().update_request(change)
    
    def delete_request(self, req_id):
        sql = "DELETE FROM requests WHERE acc_num=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [req_id])
        connection.commit()
