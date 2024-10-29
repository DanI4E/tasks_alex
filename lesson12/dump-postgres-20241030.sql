--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

-- Started on 2024-10-30 00:56:57

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 4827 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16426)
-- Name: comments; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 16425)
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 16420)
-- Name: likes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 16419)
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 16434)
-- Name: posts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 223 (class 1259 OID 16433)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 16394)
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    nationality character varying NOT NULL
);


--
-- TOC entry 217 (class 1259 OID 16393)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4819 (class 0 OID 16426)
-- Dependencies: 222
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (3, 'Cупер, советую', 1, 1);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (4, 'Надо подумать', 4, 2);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (5, 'Ура, рекомендую', 5, 4);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (6, 'Буду повторно обращаться', 2, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (7, 'Все очень плохо', 4, 3);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (8, 'Поели, попили, теперь и спать, все супер', 3, 1);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (9, '5 с плюсом', 5, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (10, 'не больше 3-х звезд', 1, 2);


--
-- TOC entry 4817 (class 0 OID 16420)
-- Dependencies: 220
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (1, 1, 2);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (2, 2, 1);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (3, 3, 5);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (4, 4, 3);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (5, 5, 4);


--
-- TOC entry 4821 (class 0 OID 16434)
-- Dependencies: 224
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (1, 'Еда', 'Вкусно и сытно', 2);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (2, 'Связь', 'Пинг большой, тяжело играть в cs', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (3, 'Красота', 'Хороший салон, много профессионалов', 4);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (4, 'Магазин', 'Много скидок, большой выбор, своя выпечка', 5);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (5, 'Техника', 'Гарантия от производителя 2 года. Приемлемые цены', 3);


--
-- TOC entry 4815 (class 0 OID 16394)
-- Dependencies: 218
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (4, 'Катя', 25, 'жен', 'русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (5, 'Лена', 18, 'жен', 'русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (1, 'Влад', 20, 'муж', 'русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (2, 'Данил', 28, 'муж', 'русский');
INSERT INTO public.users OVERRIDING SYSTEM VALUE VALUES (3, 'Антон', 45, 'муж', 'русский');


--
-- TOC entry 4828 (class 0 OID 0)
-- Dependencies: 221
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.comments_id_seq', 10, true);


--
-- TOC entry 4829 (class 0 OID 0)
-- Dependencies: 219
-- Name: likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.likes_id_seq', 5, true);


--
-- TOC entry 4830 (class 0 OID 0)
-- Dependencies: 223
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.posts_id_seq', 5, true);


--
-- TOC entry 4831 (class 0 OID 0)
-- Dependencies: 217
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- TOC entry 4661 (class 2606 OID 16432)
-- Name: comments comments_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);


--
-- TOC entry 4659 (class 2606 OID 16424)
-- Name: likes likes_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);


--
-- TOC entry 4663 (class 2606 OID 16440)
-- Name: posts posts_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);


--
-- TOC entry 4657 (class 2606 OID 16406)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- TOC entry 4666 (class 2606 OID 16467)
-- Name: comments comments_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 4667 (class 2606 OID 16452)
-- Name: comments comments_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 4664 (class 2606 OID 16462)
-- Name: likes likes_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 4665 (class 2606 OID 16447)
-- Name: likes likes_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 4668 (class 2606 OID 16457)
-- Name: posts posts_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


-- Completed on 2024-10-30 00:56:57

--
-- PostgreSQL database dump complete
--

