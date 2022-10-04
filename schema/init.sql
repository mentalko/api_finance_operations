
-- Table: public.wallet

DROP TABLE IF EXISTS public.wallet;

CREATE TABLE IF NOT EXISTS public.wallet
(
    "id"  bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    "title"  VARCHAR,
    "type_name"  VARCHAR,
    "description"  VARCHAR,
    "currency_code"  VARCHAR
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.wallet
    OWNER to postgres;



INSERT INTO public.wallet(
	 title, type_name, description, currency_code)
	VALUES ('Usual Cash', 'cash', 'my peper dollars', 'USD');

INSERT INTO public.wallet(
	 title, type_name, description, currency_code)
	VALUES ('Usual Cash', 'cash', 'my peper euros', 'EUR');

INSERT INTO public.wallet(
	 title, type_name, description, currency_code)
	VALUES ('Credit card Cash', 'credit_card', 'my bank account', 'USD');




-- Table: public.operations

DROP TABLE IF EXISTS public.operations;
CREATE TABLE IF NOT EXISTS public.operations (
	"id" 	bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
	"date"	DATE,
	"kind"	VARCHAR,
	"wallet_id" bigint,
	"amount"	NUMERIC(10, 2),
	"description"	VARCHAR,
	"operation_type"	VARCHAR
)
TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.operations
    OWNER to postgres;

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-01', 'income', 3, 12000.00, 'jan salary', 'salary');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-02', 'income', 3, 120.99, 'december 2021 cashback', 'casback');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-04', 'outcome', 3, -240.11, 'food for freege', 'supermakets');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-20', 'outcome', 3, -461.32, 'food for freege', 'supermakets');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-04', 'outcome', 3, -240.11, 'food for freege', 'supermakets');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-08', 'outcome', 3, -49.78, 'oil for car', 'transport');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-18', 'outcome', 3, -81.80, 'oil for car', 'transport');


INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-01-15', 'outcome', 3, -1200.00, 'jan rent payment', 'other');




-- 

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-01', 'income', 3, 14500.50, 'feb salary', 'salary');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-02', 'income', 3, 145.79, 'jan cashback', 'casback');




INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-10', 'outcome', 3, -480.00, 'medicine insurance', 'medicine');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-21', 'outcome', 3, -461.32, 'food for freege', 'supermakets');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-14', 'outcome', 3, -541.31, 'food for freege', 'supermakets');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-08', 'outcome', 3, -69.78, 'oil for car', 'transport');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-18', 'outcome', 3, -41.80, 'oil for car', 'transport');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-15', 'outcome', 3, -1200.00, 'jan rent payment', 'other');




INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-01', 'income', 1, 3000.00, 'снятие наличных', 'other');

INSERT INTO public.operations(
	 "date", kind, wallet_id, amount, description, operation_type) 
	VALUES ( '2022-02-15', 'outcome', 1, -120.00, 'занял другу', 'other');












