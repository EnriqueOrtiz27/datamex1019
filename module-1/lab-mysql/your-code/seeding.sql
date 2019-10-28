use lab_mysql;

INSERT INTO cars() values(001, 020, 'Volvo', 2019, 'Gray', 200000);
INSERT INTO cars() values(002, 034, 'BMW', 2015, 'Black', 400000);
INSERT INTO cars() values(003, 027, 'Ferrari', 2012, 'Red', 1000000);

INSERT INTO customers() values(001, 222, 'Carlos D.', 5540402020, 'carlos@carlos.com', 'Casa de Carlos', 'Ciudad Carlos', 'País de Carlos', 'Volvo', 020);

INSERT INTO customers() values(002, 428, 'Jonathan S.', 22244356, 'jonathan@jonathan.com', 'Casa de Jonathan', 'Atizapán', 'Mexico', 'Ferrari', 003);

INSERT INTO salespersons() values(3457, 'Jennifer', 'Madrid');
INSERT INTO salespersons() values(2459, 'Michael', 'Amsterdam');


INSERT INTO invoices() values('2010-01-15', 020, 'Volvo', 222, 3457);
INSERT INTO invoices() values('2012-05-22', 027, 'Ferrari', 428, 2459);