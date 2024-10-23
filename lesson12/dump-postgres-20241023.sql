PGDMP  "    :            	    |            postgres    17.0    17.0      �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    5    postgres    DATABASE     |   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                     postgres    false            �           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                        postgres    false    4827                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                     pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                        pg_database_owner    false    4            �            1259    16426    comments    TABLE     �   CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.comments;
       public         heap r       postgres    false    4            �            1259    16425    comments_id_seq    SEQUENCE     �   ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public               postgres    false    4    222            �            1259    16420    likes    TABLE     s   CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);
    DROP TABLE public.likes;
       public         heap r       postgres    false    4            �            1259    16419    likes_id_seq    SEQUENCE     �   ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public               postgres    false    220    4            �            1259    16434    posts    TABLE     �   CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL
);
    DROP TABLE public.posts;
       public         heap r       postgres    false    4            �            1259    16433    posts_id_seq    SEQUENCE     �   ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public               postgres    false    4    224            �            1259    16394    users    TABLE     �   CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    nationality character varying NOT NULL
);
    DROP TABLE public.users;
       public         heap r       postgres    false    4            �            1259    16393    users_id_seq    SEQUENCE     �   ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public               postgres    false    4    218            �          0    16426    comments 
   TABLE DATA                 public               postgres    false    222   j!       �          0    16420    likes 
   TABLE DATA                 public               postgres    false    220   �"       �          0    16434    posts 
   TABLE DATA                 public               postgres    false    224   ;#       �          0    16394    users 
   TABLE DATA                 public               postgres    false    218   �$       �           0    0    comments_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.comments_id_seq', 10, true);
          public               postgres    false    221            �           0    0    likes_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.likes_id_seq', 5, true);
          public               postgres    false    219            �           0    0    posts_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.posts_id_seq', 5, true);
          public               postgres    false    223            �           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 5, true);
          public               postgres    false    217            5           2606    16432    comments comments_pk 
   CONSTRAINT     R   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_pk;
       public                 postgres    false    222            3           2606    16424    likes likes_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_pk;
       public                 postgres    false    220            7           2606    16440    posts posts_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pk;
       public                 postgres    false    224            1           2606    16406    users users_pk 
   CONSTRAINT     L   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pk;
       public                 postgres    false    218            :           2606    16467    comments comments_posts_fk    FK CONSTRAINT     y   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_posts_fk;
       public               postgres    false    222    4663    224            ;           2606    16452    comments comments_users_fk    FK CONSTRAINT     y   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 D   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_users_fk;
       public               postgres    false    218    4657    222            8           2606    16462    likes likes_posts_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_posts_fk;
       public               postgres    false    220    224    4663            9           2606    16447    likes likes_users_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 >   ALTER TABLE ONLY public.likes DROP CONSTRAINT likes_users_fk;
       public               postgres    false    218    220    4657            <           2606    16457    posts posts_users_fk    FK CONSTRAINT     s   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);
 >   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_users_fk;
       public               postgres    false    224    4657    218            �   H  x����J�@��}��U!�mZ/�������B�*�����P*��@6�W8��O�7�2��|3\/p��r�~O�?]�\��Gw�������wO\�TA�9Wã����@mؖj�*J9�O���)�xٴT��a�5@t��O�(�RTR`N  �m��
�C��RJ���xªE��cH��;zGM-�J 1+i%�6�	���ڐ�'�\M
?�/��5�s*�چ�}�|�"E��҂ez�T�DЙ�Ҟ�׽A�?Gh�6���jm��:���I�m�l!�B�5n�{��~�����K6�?W�\W      �   i   x���v
Q���W((M��L����N-V�s
�t��sW�q�Us�	u���
�:
@d�i��I�F@�@S(1�XG�L)1�DG��)1���)@#�� 3]S      �   c  x��R�J�P��+f�P�k�J0H@[hb��]	��꾩�BōE�}M�HIa�<�ԍK���ܹ�s�$N͵95�N�ۋ��V�}ݹ�P�i7ΑS;&����Sj������^�"�_y�cS�g^ʝ��pJ��2���pZ�?0��ꔔ��C�\�Lk�1�#�oNy%���^X$=�f<�Uf�#��̀8�Vw��8)��[��s���ɿPw������<V}N,�����d�{�"H ��,�]|U��;�"<s���;��\�=�vi�I��@[ҵ����>ᦎY��`U�|����-��/ar�(cE�۠���x�q�/���4���G��8X#C��;%yD�� �e�5�7�b!      �   �   x���v
Q���W((M��L�+-N-*V�s
�t��sW�q�Us�	u���
&:
�f]�p��b�����)�����{�<���/6^l���;�5��<ɵl�l��6 �6���E� �']�}aÅ- ��{.6_�Fe��@OZ�h�n�U���d��{/6]�0SVqq yqͦ     