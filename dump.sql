--
-- PostgreSQL database dump
--

-- Dumped from database version 11.14 (Debian 11.14-0+deb10u1)
-- Dumped by pg_dump version 11.14 (Debian 11.14-0+deb10u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: topology; Type: SCHEMA; Schema: -; Owner: photo_user
--

CREATE SCHEMA topology;


ALTER SCHEMA topology OWNER TO photo_user;

--
-- Name: SCHEMA topology; Type: COMMENT; Schema: -; Owner: photo_user
--

COMMENT ON SCHEMA topology IS 'PostGIS Topology schema';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


--
-- Name: postgis_topology; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis_topology WITH SCHEMA topology;


--
-- Name: EXTENSION postgis_topology; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_topology IS 'PostGIS topology spatial types and functions';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accounts_procategory; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_procategory (
    id bigint NOT NULL,
    name_category character varying(50) NOT NULL
);


ALTER TABLE public.accounts_procategory OWNER TO photo_user;

--
-- Name: accounts_procategory_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_procategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_procategory_id_seq OWNER TO photo_user;

--
-- Name: accounts_procategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_procategory_id_seq OWNED BY public.accounts_procategory.id;


--
-- Name: accounts_profile; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profile (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    avatar character varying(100) NOT NULL,
    date_register timestamp with time zone NOT NULL,
    last_date_in timestamp with time zone,
    last_ip character varying(15) NOT NULL,
    work_condition character varying(100) NOT NULL,
    cost_services character varying(100) NOT NULL,
    photo_technics character varying(50) NOT NULL,
    about text,
    status integer NOT NULL,
    ready_status character varying(50) NOT NULL,
    pro_account integer,
    expired_pro_subscription timestamp with time zone,
    rating integer NOT NULL,
    location public.geometry(Point,4326),
    string_location character varying(50),
    phone character varying(15) NOT NULL,
    site character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    email_verify boolean NOT NULL,
    instagram character varying(40) NOT NULL,
    facebook character varying(40) NOT NULL,
    vk character varying(40) NOT NULL,
    location_now public.geometry(Point,4326),
    string_location_now character varying(50),
    date_stay_start timestamp with time zone,
    date_stay_end timestamp with time zone,
    message text NOT NULL,
    is_adult boolean NOT NULL,
    is_show_nu_photo boolean NOT NULL,
    is_hide boolean NOT NULL,
    views integer NOT NULL,
    last_views integer NOT NULL,
    user_channel_name character varying(255),
    type_pro_id bigint,
    user_id integer NOT NULL,
    is_change boolean NOT NULL,
    is_confirm boolean NOT NULL,
    pay_status integer NOT NULL
);


ALTER TABLE public.accounts_profile OWNER TO photo_user;

--
-- Name: accounts_profile_filming_geo; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profile_filming_geo (
    id bigint NOT NULL,
    profile_id bigint NOT NULL,
    country_id bigint NOT NULL
);


ALTER TABLE public.accounts_profile_filming_geo OWNER TO photo_user;

--
-- Name: accounts_profile_filming_geo_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profile_filming_geo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profile_filming_geo_id_seq OWNER TO photo_user;

--
-- Name: accounts_profile_filming_geo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profile_filming_geo_id_seq OWNED BY public.accounts_profile_filming_geo.id;


--
-- Name: accounts_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profile_id_seq OWNER TO photo_user;

--
-- Name: accounts_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profile_id_seq OWNED BY public.accounts_profile.id;


--
-- Name: accounts_profile_languages; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profile_languages (
    id bigint NOT NULL,
    profile_id bigint NOT NULL,
    language_id bigint NOT NULL
);


ALTER TABLE public.accounts_profile_languages OWNER TO photo_user;

--
-- Name: accounts_profile_languages_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profile_languages_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profile_languages_id_seq OWNER TO photo_user;

--
-- Name: accounts_profile_languages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profile_languages_id_seq OWNED BY public.accounts_profile_languages.id;


--
-- Name: accounts_profile_spec_model_or_photographer; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profile_spec_model_or_photographer (
    id bigint NOT NULL,
    profile_id bigint NOT NULL,
    specialization_id bigint NOT NULL
);


ALTER TABLE public.accounts_profile_spec_model_or_photographer OWNER TO photo_user;

--
-- Name: accounts_profile_spec_model_or_photographer_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profile_spec_model_or_photographer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profile_spec_model_or_photographer_id_seq OWNER TO photo_user;

--
-- Name: accounts_profile_spec_model_or_photographer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profile_spec_model_or_photographer_id_seq OWNED BY public.accounts_profile_spec_model_or_photographer.id;


--
-- Name: accounts_profilecomment; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profilecomment (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    answer_id_comment_id bigint,
    quote_id_id bigint,
    receiver_comment_id bigint NOT NULL,
    sender_comment_id bigint NOT NULL
);


ALTER TABLE public.accounts_profilecomment OWNER TO photo_user;

--
-- Name: accounts_profilecomment_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profilecomment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profilecomment_id_seq OWNER TO photo_user;

--
-- Name: accounts_profilecomment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profilecomment_id_seq OWNED BY public.accounts_profilecomment.id;


--
-- Name: accounts_profilefavorite; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profilefavorite (
    id bigint NOT NULL,
    receiver_favorite_id bigint NOT NULL,
    sender_favorite_id bigint NOT NULL
);


ALTER TABLE public.accounts_profilefavorite OWNER TO photo_user;

--
-- Name: accounts_profilefavorite_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profilefavorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profilefavorite_id_seq OWNER TO photo_user;

--
-- Name: accounts_profilefavorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profilefavorite_id_seq OWNED BY public.accounts_profilefavorite.id;


--
-- Name: accounts_profilelike; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_profilelike (
    id bigint NOT NULL,
    receiver_like_id bigint NOT NULL,
    sender_like_id bigint NOT NULL
);


ALTER TABLE public.accounts_profilelike OWNER TO photo_user;

--
-- Name: accounts_profilelike_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_profilelike_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_profilelike_id_seq OWNER TO photo_user;

--
-- Name: accounts_profilelike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_profilelike_id_seq OWNED BY public.accounts_profilelike.id;


--
-- Name: accounts_specialization; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_specialization (
    id bigint NOT NULL,
    name_spec character varying(50) NOT NULL
);


ALTER TABLE public.accounts_specialization OWNER TO photo_user;

--
-- Name: accounts_specialization_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_specialization_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_specialization_id_seq OWNER TO photo_user;

--
-- Name: accounts_specialization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_specialization_id_seq OWNED BY public.accounts_specialization.id;


--
-- Name: accounts_verificationcode; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.accounts_verificationcode (
    id bigint NOT NULL,
    email_code character varying(30),
    password_reset_token character varying(30),
    profile_id_id bigint
);


ALTER TABLE public.accounts_verificationcode OWNER TO photo_user;

--
-- Name: accounts_verificationcode_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.accounts_verificationcode_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accounts_verificationcode_id_seq OWNER TO photo_user;

--
-- Name: accounts_verificationcode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.accounts_verificationcode_id_seq OWNED BY public.accounts_verificationcode.id;


--
-- Name: additional_entities_advertisement; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_advertisement (
    id bigint NOT NULL,
    ad_image character varying(100) NOT NULL,
    ad_title character varying(255) NOT NULL,
    ad_link character varying(255) NOT NULL,
    ad_count_click integer NOT NULL
);


ALTER TABLE public.additional_entities_advertisement OWNER TO photo_user;

--
-- Name: additional_entities_advertisement_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_advertisement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_advertisement_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_advertisement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_advertisement_id_seq OWNED BY public.additional_entities_advertisement.id;


--
-- Name: additional_entities_answer; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_answer (
    id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    choice_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.additional_entities_answer OWNER TO photo_user;

--
-- Name: additional_entities_answer_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_answer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_answer_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_answer_id_seq OWNED BY public.additional_entities_answer.id;


--
-- Name: additional_entities_banword; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_banword (
    id bigint NOT NULL,
    word character varying(45) NOT NULL
);


ALTER TABLE public.additional_entities_banword OWNER TO photo_user;

--
-- Name: additional_entities_banword_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_banword_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_banword_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_banword_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_banword_id_seq OWNED BY public.additional_entities_banword.id;


--
-- Name: additional_entities_choice; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_choice (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    question_id bigint NOT NULL
);


ALTER TABLE public.additional_entities_choice OWNER TO photo_user;

--
-- Name: additional_entities_choice_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_choice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_choice_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_choice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_choice_id_seq OWNED BY public.additional_entities_choice.id;


--
-- Name: additional_entities_city; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_city (
    id bigint NOT NULL,
    city_name character varying(50) NOT NULL,
    coordinates character varying(50) NOT NULL,
    country_id bigint NOT NULL
);


ALTER TABLE public.additional_entities_city OWNER TO photo_user;

--
-- Name: additional_entities_city_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_city_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_city_id_seq OWNED BY public.additional_entities_city.id;


--
-- Name: additional_entities_country; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_country (
    id bigint NOT NULL,
    name_country character varying(45) NOT NULL
);


ALTER TABLE public.additional_entities_country OWNER TO photo_user;

--
-- Name: additional_entities_country_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_country_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_country_id_seq OWNED BY public.additional_entities_country.id;


--
-- Name: additional_entities_customsettings; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_customsettings (
    id bigint NOT NULL,
    distance_for_unique_places integer NOT NULL,
    days_request_to_not_auth_user integer NOT NULL
);


ALTER TABLE public.additional_entities_customsettings OWNER TO photo_user;

--
-- Name: additional_entities_customsettings_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_customsettings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_customsettings_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_customsettings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_customsettings_id_seq OWNED BY public.additional_entities_customsettings.id;


--
-- Name: additional_entities_emailfragment; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_emailfragment (
    id bigint NOT NULL,
    verify_email text,
    reset_password text,
    verify_email_for_not_auth_request text
);


ALTER TABLE public.additional_entities_emailfragment OWNER TO photo_user;

--
-- Name: additional_entities_emailfragment_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_emailfragment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_emailfragment_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_emailfragment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_emailfragment_id_seq OWNED BY public.additional_entities_emailfragment.id;


--
-- Name: additional_entities_language; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_language (
    id bigint NOT NULL,
    name_language character varying(15) NOT NULL
);


ALTER TABLE public.additional_entities_language OWNER TO photo_user;

--
-- Name: additional_entities_language_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_language_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_language_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_language_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_language_id_seq OWNED BY public.additional_entities_language.id;


--
-- Name: additional_entities_question; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.additional_entities_question (
    id bigint NOT NULL,
    title character varying(255) NOT NULL,
    is_hide boolean NOT NULL
);


ALTER TABLE public.additional_entities_question OWNER TO photo_user;

--
-- Name: additional_entities_question_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.additional_entities_question_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.additional_entities_question_id_seq OWNER TO photo_user;

--
-- Name: additional_entities_question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.additional_entities_question_id_seq OWNED BY public.additional_entities_question.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO photo_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO photo_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO photo_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO photo_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO photo_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO photo_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO photo_user;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO photo_user;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO photo_user;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO photo_user;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO photo_user;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO photo_user;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: chat_chat; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.chat_chat (
    id bigint NOT NULL,
    receiver_id_id bigint NOT NULL,
    sender_id_id bigint NOT NULL,
    is_receiver_hide_chat boolean NOT NULL,
    is_sender_hide_chat boolean NOT NULL
);


ALTER TABLE public.chat_chat OWNER TO photo_user;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.chat_chat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_chat_id_seq OWNER TO photo_user;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.chat_chat_id_seq OWNED BY public.chat_chat.id;


--
-- Name: chat_message; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.chat_message (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    status_read boolean NOT NULL,
    author_id bigint NOT NULL,
    chat_id bigint NOT NULL
);


ALTER TABLE public.chat_message OWNER TO photo_user;

--
-- Name: chat_message_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.chat_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_message_id_seq OWNER TO photo_user;

--
-- Name: chat_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.chat_message_id_seq OWNED BY public.chat_message.id;


--
-- Name: chat_notification; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.chat_notification (
    id bigint NOT NULL,
    type_note character varying(25),
    text_note text,
    is_read boolean,
    "timestamp" timestamp with time zone NOT NULL,
    model_id integer NOT NULL,
    receiver_id bigint,
    sender_id bigint
);


ALTER TABLE public.chat_notification OWNER TO photo_user;

--
-- Name: chat_notification_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.chat_notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_notification_id_seq OWNER TO photo_user;

--
-- Name: chat_notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.chat_notification_id_seq OWNED BY public.chat_notification.id;


--
-- Name: chat_requestchat; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.chat_requestchat (
    id bigint NOT NULL,
    request_receiver_id bigint NOT NULL,
    request_sender_id bigint NOT NULL
);


ALTER TABLE public.chat_requestchat OWNER TO photo_user;

--
-- Name: chat_requestchat_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.chat_requestchat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_requestchat_id_seq OWNER TO photo_user;

--
-- Name: chat_requestchat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.chat_requestchat_id_seq OWNED BY public.chat_requestchat.id;


--
-- Name: chat_requestmessage; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.chat_requestmessage (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    status_read boolean NOT NULL,
    author_id bigint NOT NULL,
    chat_id bigint NOT NULL,
    request_id bigint
);


ALTER TABLE public.chat_requestmessage OWNER TO photo_user;

--
-- Name: chat_requestmessage_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.chat_requestmessage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_requestmessage_id_seq OWNER TO photo_user;

--
-- Name: chat_requestmessage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.chat_requestmessage_id_seq OWNED BY public.chat_requestmessage.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO photo_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO photo_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO photo_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO photo_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO photo_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO photo_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO photo_user;

--
-- Name: film_places_categoryfilmplaces; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_categoryfilmplaces (
    id bigint NOT NULL,
    name_category character varying(40) NOT NULL
);


ALTER TABLE public.film_places_categoryfilmplaces OWNER TO photo_user;

--
-- Name: film_places_categoryfilmplaces_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_categoryfilmplaces_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_categoryfilmplaces_id_seq OWNER TO photo_user;

--
-- Name: film_places_categoryfilmplaces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_categoryfilmplaces_id_seq OWNED BY public.film_places_categoryfilmplaces.id;


--
-- Name: film_places_filmplaces; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplaces (
    id bigint NOT NULL,
    name_place character varying(50) NOT NULL,
    description text NOT NULL,
    photo_camera character varying(40) NOT NULL,
    cost character varying(10) NOT NULL,
    payment character varying(40) NOT NULL,
    place_location public.geometry(Point,4326) NOT NULL,
    string_place_location character varying(40),
    views integer NOT NULL,
    last_views integer NOT NULL,
    last_ip_user character varying(18),
    is_hidden boolean NOT NULL,
    was_added timestamp with time zone NOT NULL,
    main_photo_id bigint,
    profile_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplaces OWNER TO photo_user;

--
-- Name: film_places_filmplaces_category; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplaces_category (
    id bigint NOT NULL,
    filmplaces_id bigint NOT NULL,
    categoryfilmplaces_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplaces_category OWNER TO photo_user;

--
-- Name: film_places_filmplaces_category_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplaces_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplaces_category_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplaces_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplaces_category_id_seq OWNED BY public.film_places_filmplaces_category.id;


--
-- Name: film_places_filmplaces_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplaces_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplaces_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplaces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplaces_id_seq OWNED BY public.film_places_filmplaces.id;


--
-- Name: film_places_filmplaces_place_image; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplaces_place_image (
    id bigint NOT NULL,
    filmplaces_id bigint NOT NULL,
    image_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplaces_place_image OWNER TO photo_user;

--
-- Name: film_places_filmplaces_place_image_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplaces_place_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplaces_place_image_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplaces_place_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplaces_place_image_id_seq OWNED BY public.film_places_filmplaces_place_image.id;


--
-- Name: film_places_filmplacescomment; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplacescomment (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    answer_id_comment_id bigint,
    place_id bigint NOT NULL,
    quote_id_id bigint,
    sender_comment_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplacescomment OWNER TO photo_user;

--
-- Name: film_places_filmplacescomment_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplacescomment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplacescomment_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplacescomment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplacescomment_id_seq OWNED BY public.film_places_filmplacescomment.id;


--
-- Name: film_places_filmplacesfavorite; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplacesfavorite (
    id bigint NOT NULL,
    place_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplacesfavorite OWNER TO photo_user;

--
-- Name: film_places_filmplacesfavorite_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplacesfavorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplacesfavorite_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplacesfavorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplacesfavorite_id_seq OWNED BY public.film_places_filmplacesfavorite.id;


--
-- Name: film_places_filmplaceslike; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmplaceslike (
    id bigint NOT NULL,
    place_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.film_places_filmplaceslike OWNER TO photo_user;

--
-- Name: film_places_filmplaceslike_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmplaceslike_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmplaceslike_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmplaceslike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmplaceslike_id_seq OWNED BY public.film_places_filmplaceslike.id;


--
-- Name: film_places_filmrequest; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_filmrequest (
    id bigint NOT NULL,
    filming_timestamp timestamp with time zone NOT NULL,
    hours_duration character varying(40) NOT NULL,
    filming_type character varying(40) NOT NULL,
    filming_status character varying(12) NOT NULL,
    count_person character varying(40) NOT NULL,
    filming_budget character varying(40) NOT NULL,
    need_makeup_artist boolean NOT NULL,
    description text NOT NULL,
    was_added timestamp with time zone NOT NULL,
    profile_id bigint NOT NULL,
    place_filming character varying(40),
    receiver_profile_id bigint,
    reason_failure text
);


ALTER TABLE public.film_places_filmrequest OWNER TO photo_user;

--
-- Name: film_places_filmrequest_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_filmrequest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_filmrequest_id_seq OWNER TO photo_user;

--
-- Name: film_places_filmrequest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_filmrequest_id_seq OWNED BY public.film_places_filmrequest.id;


--
-- Name: film_places_notauthfilmrequest; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.film_places_notauthfilmrequest (
    id bigint NOT NULL,
    filming_timestamp timestamp with time zone NOT NULL,
    hours_duration character varying(40) NOT NULL,
    filming_type character varying(40) NOT NULL,
    count_person character varying(40) NOT NULL,
    filming_budget character varying(40) NOT NULL,
    need_makeup_artist boolean NOT NULL,
    description text NOT NULL,
    was_added timestamp with time zone NOT NULL,
    place_filming character varying(40) NOT NULL,
    email character varying(40) NOT NULL,
    email_verify boolean NOT NULL,
    email_code character varying(40) NOT NULL,
    receiver_profile_id bigint NOT NULL
);


ALTER TABLE public.film_places_notauthfilmrequest OWNER TO photo_user;

--
-- Name: film_places_notauthfilmrequest_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.film_places_notauthfilmrequest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_places_notauthfilmrequest_id_seq OWNER TO photo_user;

--
-- Name: film_places_notauthfilmrequest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.film_places_notauthfilmrequest_id_seq OWNED BY public.film_places_notauthfilmrequest.id;


--
-- Name: gallery_album; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_album (
    id bigint NOT NULL,
    name_album character varying(40) NOT NULL,
    description_album text NOT NULL,
    is_hidden boolean NOT NULL,
    main_photo_id_id bigint,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_album OWNER TO photo_user;

--
-- Name: gallery_album_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_album_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_album_id_seq OWNER TO photo_user;

--
-- Name: gallery_album_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_album_id_seq OWNED BY public.gallery_album.id;


--
-- Name: gallery_gallery; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_gallery (
    id bigint NOT NULL,
    name_image character varying(50) NOT NULL,
    description text NOT NULL,
    place_location public.geometry(Point,4326) NOT NULL,
    string_place_location character varying(40),
    tags text,
    photo_camera character varying(40) NOT NULL,
    focal_len character varying(40) NOT NULL,
    excerpt character varying(40) NOT NULL,
    aperture character varying(40),
    iso character varying(40),
    flash character varying(40) NOT NULL,
    is_sell boolean NOT NULL,
    last_ip_user character varying(18),
    views integer NOT NULL,
    was_added timestamp with time zone NOT NULL,
    is_hidden boolean NOT NULL,
    gallery_image_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_gallery OWNER TO photo_user;

--
-- Name: gallery_gallery_album; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_gallery_album (
    id bigint NOT NULL,
    gallery_id bigint NOT NULL,
    album_id bigint NOT NULL
);


ALTER TABLE public.gallery_gallery_album OWNER TO photo_user;

--
-- Name: gallery_gallery_album_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_gallery_album_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_gallery_album_id_seq OWNER TO photo_user;

--
-- Name: gallery_gallery_album_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_gallery_album_id_seq OWNED BY public.gallery_gallery_album.id;


--
-- Name: gallery_gallery_category; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_gallery_category (
    id bigint NOT NULL,
    gallery_id bigint NOT NULL,
    specialization_id bigint NOT NULL
);


ALTER TABLE public.gallery_gallery_category OWNER TO photo_user;

--
-- Name: gallery_gallery_category_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_gallery_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_gallery_category_id_seq OWNER TO photo_user;

--
-- Name: gallery_gallery_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_gallery_category_id_seq OWNED BY public.gallery_gallery_category.id;


--
-- Name: gallery_gallery_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_gallery_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_gallery_id_seq OWNER TO photo_user;

--
-- Name: gallery_gallery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_gallery_id_seq OWNED BY public.gallery_gallery.id;


--
-- Name: gallery_gallerycomment; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_gallerycomment (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    answer_id_comment_id bigint,
    gallery_id bigint NOT NULL,
    quote_id_id bigint,
    sender_comment_id bigint NOT NULL
);


ALTER TABLE public.gallery_gallerycomment OWNER TO photo_user;

--
-- Name: gallery_gallerycomment_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_gallerycomment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_gallerycomment_id_seq OWNER TO photo_user;

--
-- Name: gallery_gallerycomment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_gallerycomment_id_seq OWNED BY public.gallery_gallerycomment.id;


--
-- Name: gallery_galleryfavorite; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_galleryfavorite (
    id bigint NOT NULL,
    gallery_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_galleryfavorite OWNER TO photo_user;

--
-- Name: gallery_galleryfavorite_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_galleryfavorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_galleryfavorite_id_seq OWNER TO photo_user;

--
-- Name: gallery_galleryfavorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_galleryfavorite_id_seq OWNED BY public.gallery_galleryfavorite.id;


--
-- Name: gallery_gallerylike; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_gallerylike (
    id bigint NOT NULL,
    gallery_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_gallerylike OWNER TO photo_user;

--
-- Name: gallery_gallerylike_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_gallerylike_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_gallerylike_id_seq OWNER TO photo_user;

--
-- Name: gallery_gallerylike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_gallerylike_id_seq OWNED BY public.gallery_gallerylike.id;


--
-- Name: gallery_image; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_image (
    id bigint NOT NULL,
    photo character varying(100) NOT NULL,
    profile_id bigint
);


ALTER TABLE public.gallery_image OWNER TO photo_user;

--
-- Name: gallery_image_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_image_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_image_id_seq OWNER TO photo_user;

--
-- Name: gallery_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_image_id_seq OWNED BY public.gallery_image.id;


--
-- Name: gallery_photosession; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_photosession (
    id bigint NOT NULL,
    session_name character varying(40) NOT NULL,
    session_description text NOT NULL,
    session_location public.geometry(Point,4326) NOT NULL,
    string_session_location character varying(40),
    session_date date NOT NULL,
    last_ip_user character varying(18),
    views integer NOT NULL,
    is_hidden boolean NOT NULL,
    main_photo_id bigint,
    profile_id bigint NOT NULL,
    session_category_id bigint
);


ALTER TABLE public.gallery_photosession OWNER TO photo_user;

--
-- Name: gallery_photosession_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_photosession_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_photosession_id_seq OWNER TO photo_user;

--
-- Name: gallery_photosession_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_photosession_id_seq OWNED BY public.gallery_photosession.id;


--
-- Name: gallery_photosession_photos; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_photosession_photos (
    id bigint NOT NULL,
    photosession_id bigint NOT NULL,
    image_id bigint NOT NULL
);


ALTER TABLE public.gallery_photosession_photos OWNER TO photo_user;

--
-- Name: gallery_photosession_photos_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_photosession_photos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_photosession_photos_id_seq OWNER TO photo_user;

--
-- Name: gallery_photosession_photos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_photosession_photos_id_seq OWNED BY public.gallery_photosession_photos.id;


--
-- Name: gallery_photosessioncomment; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_photosessioncomment (
    id bigint NOT NULL,
    content text NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    answer_id_comment_id bigint,
    photo_session_id bigint NOT NULL,
    quote_id_id bigint,
    sender_comment_id bigint NOT NULL
);


ALTER TABLE public.gallery_photosessioncomment OWNER TO photo_user;

--
-- Name: gallery_photosessioncomment_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_photosessioncomment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_photosessioncomment_id_seq OWNER TO photo_user;

--
-- Name: gallery_photosessioncomment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_photosessioncomment_id_seq OWNED BY public.gallery_photosessioncomment.id;


--
-- Name: gallery_photosessionfavorite; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_photosessionfavorite (
    id bigint NOT NULL,
    photo_session_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_photosessionfavorite OWNER TO photo_user;

--
-- Name: gallery_photosessionfavorite_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_photosessionfavorite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_photosessionfavorite_id_seq OWNER TO photo_user;

--
-- Name: gallery_photosessionfavorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_photosessionfavorite_id_seq OWNED BY public.gallery_photosessionfavorite.id;


--
-- Name: gallery_photosessionlike; Type: TABLE; Schema: public; Owner: photo_user
--

CREATE TABLE public.gallery_photosessionlike (
    id bigint NOT NULL,
    photo_session_id bigint NOT NULL,
    profile_id bigint NOT NULL
);


ALTER TABLE public.gallery_photosessionlike OWNER TO photo_user;

--
-- Name: gallery_photosessionlike_id_seq; Type: SEQUENCE; Schema: public; Owner: photo_user
--

CREATE SEQUENCE public.gallery_photosessionlike_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gallery_photosessionlike_id_seq OWNER TO photo_user;

--
-- Name: gallery_photosessionlike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: photo_user
--

ALTER SEQUENCE public.gallery_photosessionlike_id_seq OWNED BY public.gallery_photosessionlike.id;


--
-- Name: accounts_procategory id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_procategory ALTER COLUMN id SET DEFAULT nextval('public.accounts_procategory_id_seq'::regclass);


--
-- Name: accounts_profile id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile ALTER COLUMN id SET DEFAULT nextval('public.accounts_profile_id_seq'::regclass);


--
-- Name: accounts_profile_filming_geo id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_filming_geo ALTER COLUMN id SET DEFAULT nextval('public.accounts_profile_filming_geo_id_seq'::regclass);


--
-- Name: accounts_profile_languages id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_languages ALTER COLUMN id SET DEFAULT nextval('public.accounts_profile_languages_id_seq'::regclass);


--
-- Name: accounts_profile_spec_model_or_photographer id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_spec_model_or_photographer ALTER COLUMN id SET DEFAULT nextval('public.accounts_profile_spec_model_or_photographer_id_seq'::regclass);


--
-- Name: accounts_profilecomment id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment ALTER COLUMN id SET DEFAULT nextval('public.accounts_profilecomment_id_seq'::regclass);


--
-- Name: accounts_profilefavorite id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilefavorite ALTER COLUMN id SET DEFAULT nextval('public.accounts_profilefavorite_id_seq'::regclass);


--
-- Name: accounts_profilelike id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilelike ALTER COLUMN id SET DEFAULT nextval('public.accounts_profilelike_id_seq'::regclass);


--
-- Name: accounts_specialization id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_specialization ALTER COLUMN id SET DEFAULT nextval('public.accounts_specialization_id_seq'::regclass);


--
-- Name: accounts_verificationcode id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_verificationcode ALTER COLUMN id SET DEFAULT nextval('public.accounts_verificationcode_id_seq'::regclass);


--
-- Name: additional_entities_advertisement id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_advertisement ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_advertisement_id_seq'::regclass);


--
-- Name: additional_entities_answer id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_answer ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_answer_id_seq'::regclass);


--
-- Name: additional_entities_banword id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_banword ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_banword_id_seq'::regclass);


--
-- Name: additional_entities_choice id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_choice ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_choice_id_seq'::regclass);


--
-- Name: additional_entities_city id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_city ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_city_id_seq'::regclass);


--
-- Name: additional_entities_country id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_country ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_country_id_seq'::regclass);


--
-- Name: additional_entities_customsettings id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_customsettings ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_customsettings_id_seq'::regclass);


--
-- Name: additional_entities_emailfragment id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_emailfragment ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_emailfragment_id_seq'::regclass);


--
-- Name: additional_entities_language id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_language ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_language_id_seq'::regclass);


--
-- Name: additional_entities_question id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_question ALTER COLUMN id SET DEFAULT nextval('public.additional_entities_question_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: chat_chat id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_chat ALTER COLUMN id SET DEFAULT nextval('public.chat_chat_id_seq'::regclass);


--
-- Name: chat_message id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_message ALTER COLUMN id SET DEFAULT nextval('public.chat_message_id_seq'::regclass);


--
-- Name: chat_notification id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_notification ALTER COLUMN id SET DEFAULT nextval('public.chat_notification_id_seq'::regclass);


--
-- Name: chat_requestchat id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestchat ALTER COLUMN id SET DEFAULT nextval('public.chat_requestchat_id_seq'::regclass);


--
-- Name: chat_requestmessage id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestmessage ALTER COLUMN id SET DEFAULT nextval('public.chat_requestmessage_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: film_places_categoryfilmplaces id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_categoryfilmplaces ALTER COLUMN id SET DEFAULT nextval('public.film_places_categoryfilmplaces_id_seq'::regclass);


--
-- Name: film_places_filmplaces id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplaces_id_seq'::regclass);


--
-- Name: film_places_filmplaces_category id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_category ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplaces_category_id_seq'::regclass);


--
-- Name: film_places_filmplaces_place_image id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_place_image ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplaces_place_image_id_seq'::regclass);


--
-- Name: film_places_filmplacescomment id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplacescomment_id_seq'::regclass);


--
-- Name: film_places_filmplacesfavorite id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacesfavorite ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplacesfavorite_id_seq'::regclass);


--
-- Name: film_places_filmplaceslike id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaceslike ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmplaceslike_id_seq'::regclass);


--
-- Name: film_places_filmrequest id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmrequest ALTER COLUMN id SET DEFAULT nextval('public.film_places_filmrequest_id_seq'::regclass);


--
-- Name: film_places_notauthfilmrequest id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_notauthfilmrequest ALTER COLUMN id SET DEFAULT nextval('public.film_places_notauthfilmrequest_id_seq'::regclass);


--
-- Name: gallery_album id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_album ALTER COLUMN id SET DEFAULT nextval('public.gallery_album_id_seq'::regclass);


--
-- Name: gallery_gallery id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery ALTER COLUMN id SET DEFAULT nextval('public.gallery_gallery_id_seq'::regclass);


--
-- Name: gallery_gallery_album id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_album ALTER COLUMN id SET DEFAULT nextval('public.gallery_gallery_album_id_seq'::regclass);


--
-- Name: gallery_gallery_category id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_category ALTER COLUMN id SET DEFAULT nextval('public.gallery_gallery_category_id_seq'::regclass);


--
-- Name: gallery_gallerycomment id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment ALTER COLUMN id SET DEFAULT nextval('public.gallery_gallerycomment_id_seq'::regclass);


--
-- Name: gallery_galleryfavorite id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_galleryfavorite ALTER COLUMN id SET DEFAULT nextval('public.gallery_galleryfavorite_id_seq'::regclass);


--
-- Name: gallery_gallerylike id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerylike ALTER COLUMN id SET DEFAULT nextval('public.gallery_gallerylike_id_seq'::regclass);


--
-- Name: gallery_image id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_image ALTER COLUMN id SET DEFAULT nextval('public.gallery_image_id_seq'::regclass);


--
-- Name: gallery_photosession id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession ALTER COLUMN id SET DEFAULT nextval('public.gallery_photosession_id_seq'::regclass);


--
-- Name: gallery_photosession_photos id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession_photos ALTER COLUMN id SET DEFAULT nextval('public.gallery_photosession_photos_id_seq'::regclass);


--
-- Name: gallery_photosessioncomment id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment ALTER COLUMN id SET DEFAULT nextval('public.gallery_photosessioncomment_id_seq'::regclass);


--
-- Name: gallery_photosessionfavorite id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionfavorite ALTER COLUMN id SET DEFAULT nextval('public.gallery_photosessionfavorite_id_seq'::regclass);


--
-- Name: gallery_photosessionlike id; Type: DEFAULT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionlike ALTER COLUMN id SET DEFAULT nextval('public.gallery_photosessionlike_id_seq'::regclass);


--
-- Data for Name: accounts_procategory; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_procategory (id, name_category) FROM stdin;
1	Фотографы
2	Визажисты
3	Модели
4	Фотостудии
5	Фотопечать
6	Аренда
7	Видеографы
8	Фотошколы
9	Ретушеры
10	Декораторы
11	Организатор
\.


--
-- Data for Name: accounts_profile; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profile (id, name, surname, avatar, date_register, last_date_in, last_ip, work_condition, cost_services, photo_technics, about, status, ready_status, pro_account, expired_pro_subscription, rating, location, string_location, phone, site, email, email_verify, instagram, facebook, vk, location_now, string_location_now, date_stay_start, date_stay_end, message, is_adult, is_show_nu_photo, is_hide, views, last_views, user_channel_name, type_pro_id, user_id, is_change, is_confirm, pay_status) FROM stdin;
1	Vlad	admin	default_images/anonymous.jpg	2022-04-05 10:08:31+00	2022-04-08 10:36:16.462651+00	37.214.34.246					1		1	\N	0	\N	1	1		draculatvink@gmail.com	t				\N	1	\N	\N		f	f	f	10	10	\N	\N	1	f	f	0
2	Эдуард	Баринов	default_images/anonymous.jpg	2022-04-06 15:27:09.639627+00	2022-04-06 15:27:10.305556+00	79.170.109.191				\N	2		1	\N	0	\N	\N			muzhyke1@gmail.com	f				\N	\N	\N	\N		t	f	f	0	0	\N	\N	2	f	f	0
6	test	test	default_images/anonymous.jpg	2022-04-07 09:47:20.126324+00	2022-05-11 16:34:32.753418+00	37.214.41.137	тест	цу	уцу	авыавы	2		1	\N	0	0101000020E61000008729B29BA0DE4B40080951BE420F4340	Россия, Московская область	+375296732364	нпргшргш	tsp7439@gmail.com	t				0101000020E61000001A0D2B22E3EC4B40080951BE48094340	Россия, Московская область	2022-04-13 21:00:00+00	2022-04-09 21:00:00+00		t	f	f	0	0	\N	3	6	t	f	0
11	1	2	default_images/anonymous.jpg	2022-04-16 15:28:13.589217+00	2022-04-16 15:28:14.108641+00	95.54.99.69				\N	1		1	\N	0	\N	\N			EEEE@MAIL.COM	f				\N	\N	\N	\N		f	f	f	0	0	\N	\N	11	f	f	0
8	Эдуард	Баринов	avatars/4673110d-4ca.png	2022-04-07 14:06:56.94046+00	2022-05-06 11:04:43.872135+00	79.170.109.191	лалала	5000	лалала	ываыва	2	Все ок	1	\N	0	0101000020E61000007702BB61D3DE4B40070951BE68F84240	Россия, Московская область	ываы	ыва	joffreyprogamer@gmail.com	t				0101000020E6100000D35B86883FF04B40090951BE34E14240	Россия, Московская область	2022-04-06 21:00:00+00	2022-04-23 21:00:00+00	фываыфвп	t	f	f	0	0	\N	1	8	t	f	0
9	Эдуард	Баринов	avatars/c4c49c32-e2c.png	2022-04-08 16:59:26.531752+00	2022-04-12 15:13:17.011833+00	87.252.225.217	тест	5000	тест		2		1	\N	0	0101000020E61000006A83CBB5F8D84B40090951BE5A9D4240	Россия, Московская область			muzhyke@gmail.com	t				0101000020E6100000D254FD099DD24B40090951BEF4A84240	Россия, Москва	2022-04-18 21:00:00+00	2022-04-27 21:00:00+00	тест	t	f	f	0	0	\N	1	9	t	f	0
10	Test	Testov	avatars/600b1521-fd5.jpg	2022-04-08 17:34:37+00	2022-05-13 13:03:45.655747+00	91.245.140.119	За деньги	100р	кэнон	Про меня. Тест.	2		1	\N	0	0101000020E6100000A4D9F14DCDD24940060951BE12994340	Россия, Воронеж	+79268333366	photodel.ru/	profotki@mail.ru	t				0101000020E610000000EA3A34992A4C40040951BE10024640	Россия, Нижний Новгород	2022-05-13 21:00:00+00	2022-05-28 20:59:59+00	1\r\n2\r\n3	t	f	f	0	0	\N	1	10	t	f	0
12	артем	аврменко	default_images/anonymous.jpg	2022-04-28 18:22:34.617779+00	2022-04-28 18:22:35.190248+00	37.214.72.159				\N	2		1	\N	0	\N	\N			avramenkoa773@gmail.com	f				\N	\N	\N	\N		t	f	f	0	0	\N	\N	12	f	f	0
7	Эдуард	Баринов	avatars/52f0440f-6ae.jpg	2022-04-07 11:41:59.792669+00	2022-05-13 09:18:17.2903+00	46.56.202.207	фыва	ыва	фыва	фыва	2	статус	1	\N	0	0101000020E610000030FFD8C877D94B40080951BE7ED34240	Россия, Москва	фыва	фыва	joffreywebd@gmail.com	t				0101000020E610000030FFD8C877D94B40070951BE76724240	Россия, Московская область	2022-04-10 21:00:00+00	2022-04-17 20:59:59+00	фыва	t	f	f	0	0	\N	1	7	t	f	0
15	Мария	Бирюкова	default_images/anonymous.jpg	2022-05-13 09:44:20.340251+00	2022-05-13 10:06:58.429447+00	5.130.138.210				\N	2		1	\N	0	\N	\N			masiasia@narod.ru	t				\N	\N	\N	\N		t	f	f	0	0	\N	\N	15	f	f	0
14	Артем	Синепалов	default_images/anonymous.jpg	2022-05-13 09:18:53.710466+00	2022-05-13 11:39:32.516508+00	79.170.109.191	test	5.000	test	test	2		1	\N	0	0101000020E610000018BC9201CFE04B40060951BE86DA4240	Россия, Москва	test	test	leksich3@gmail.com	t				0101000020E61000007B566EE1BFCB4B40080951BE28ED4240	Россия, Московская область	1970-01-15 21:00:00+00	1970-01-20 20:59:59+00	test	t	f	f	0	0	specific..inmemory!DUGcLpbDriRl	1	14	t	f	0
13	Вячеслав	Туман	default_images/anonymous.jpg	2022-05-10 10:21:20.125836+00	2022-05-10 10:28:58.627308+00	83.220.238.7				\N	1		1	\N	0	\N	\N			Slava_tuman@mail.ru	t				\N	\N	\N	\N		t	f	f	0	0	\N	\N	13	f	f	0
\.


--
-- Data for Name: accounts_profile_filming_geo; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profile_filming_geo (id, profile_id, country_id) FROM stdin;
1	7	3
2	6	1
3	8	2
4	9	3
\.


--
-- Data for Name: accounts_profile_languages; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profile_languages (id, profile_id, language_id) FROM stdin;
1	7	1
2	6	3
3	8	1
4	10	1
5	10	4
\.


--
-- Data for Name: accounts_profile_spec_model_or_photographer; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profile_spec_model_or_photographer (id, profile_id, specialization_id) FROM stdin;
1	7	20
2	6	17
3	6	20
4	8	18
5	9	20
6	10	2
\.


--
-- Data for Name: accounts_profilecomment; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profilecomment (id, content, "timestamp", answer_id_comment_id, quote_id_id, receiver_comment_id, sender_comment_id) FROM stdin;
\.


--
-- Data for Name: accounts_profilefavorite; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profilefavorite (id, receiver_favorite_id, sender_favorite_id) FROM stdin;
1	6	7
2	7	7
3	10	10
4	9	10
5	8	10
6	7	10
\.


--
-- Data for Name: accounts_profilelike; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_profilelike (id, receiver_like_id, sender_like_id) FROM stdin;
\.


--
-- Data for Name: accounts_specialization; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_specialization (id, name_spec) FROM stdin;
1	Животные
2	Архитектура
3	Репортаж
4	Дети
5	Семья
6	Беременные
7	Аэросъемки
8	Видеосъемка
9	Интерьеры
10	Новорожденные
11	Обучение фотографии
12	Портрет
13	Предметная съемка
14	Каталожная съемка
15	Реклама
16	Свадебные
17	Food
18	Love Story
19	Ню
20	3d фотографы
\.


--
-- Data for Name: accounts_verificationcode; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.accounts_verificationcode (id, email_code, password_reset_token, profile_id_id) FROM stdin;
1	xGEVrXaFdtunFdofqwiY1BfEaslxVd	\N	2
6	eO1otMQlrJtOEVxiFNoYAZuTBvNOio	\N	6
7	TGoIVQUkuvBCtufSjcjuJv1jPwaw8i	\N	7
8	vgoeJgG6nSHDY28VD2ChBWwglv96TF	\N	8
5	J5f1WZctEKZYQuWfjR3HDFXGksJ7cV	\N	1
9	8U1qaUwBoW8uy5iJu0cYqiEr7ahHR3	\N	9
10	qNSFgu2ETjFqxaf0Dxczsi8CRPiCpT	\N	10
11	SeHwWF0HS94AIFt7iwXajVpwVwp0ed	\N	11
12	Joh0rWcCGTaKHdhZPnyQjqdarCH7QF	\N	12
13	TQGSzRoqq5Ew1TZhRSKnCoJEVZJqIw	\N	13
14	ofgXrptiF1HUpszf3txWK4nVk4HUSs	\N	14
15	3vsMTfIROj0q2pHec7f6aUYit4j2Dx	\N	15
\.


--
-- Data for Name: additional_entities_advertisement; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_advertisement (id, ad_image, ad_title, ad_link, ad_count_click) FROM stdin;
1	ad/Котята.jpg	Тест блока	https://photodel.ru/photos	0
\.


--
-- Data for Name: additional_entities_answer; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_answer (id, created, choice_id, profile_id) FROM stdin;
\.


--
-- Data for Name: additional_entities_banword; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_banword (id, word) FROM stdin;
1	апездал
2	апездошенная
3	архипиздрит
4	басран
5	бздение
6	бздеть
7	бздех
8	бзднуть
9	бздун
10	бздунья
11	бздюха
12	бикса
13	блежник
14	блудилище
15	блябу
16	блябуду
17	бляд
18	блядство
19	блядун
20	блядунья
21	блядь
22	блядюга
23	взьебка
24	взьебывать
25	волосянка
26	вхуюжить
27	выблядок
28	выблядыш
29	выебать
30	выебон
31	выебать
32	выпердеть
33	высраться
34	выссаться
35	говенка
36	говенный
37	говешка
38	говназия
39	говнецо
40	говно
41	говноед
42	говночист
43	говнюк
44	говнюха
45	говнядина
46	говняк
47	говняный
48	говнять
49	гомосек
50	гондон
51	дермо
52	долбоеб
53	долбоёб
54	дрисня
55	дрист
56	дристануть
57	дристать
58	дристун
59	дристуха
60	дрочена
61	дрочила
62	дрочилка
63	дрочить
64	дрочка
65	ебало
66	ебальник
67	ебануть
68	ебаный
69	ебарь
70	ебатория
71	ебать
72	ебаться
73	ебец
74	ебическая
75	еблан
76	ебливый
77	еблище
78	ебло
79	ебля
80	ебнуть
81	ёбнуть
82	ебнуться
83	ебня
84	ёболызнуть
85	ебош
86	ебун
87	ебунок
88	ебывать
89	елда
90	елдак
91	елдачить
92	заговнять
93	задристать
94	задрока
95	заёб
96	заеба
97	заебал
98	заебанец
99	заебатый
100	заебать
101	заебаться
102	заебываться
103	заеть
104	залупа
105	залупаться
106	залупить
107	залупиться
108	замудохаться
109	засерать
110	засерун
111	засеря
112	засирать
113	засранец
114	засрун
115	захуячить
116	злаебучий
117	злоебучий
118	иди
119	изговнять
120	изговняться
121	кляпыжиться
122	колдоебина
123	курва
124	курвенок
125	курвин
126	курвяжник
127	курвяжница
128	курвяжный
129	манда
130	мандавошка
131	мандей
132	мандеть
133	мандища
134	мандовошка
135	мандюк
136	минет
137	минетчик
138	минетчица
139	мокрохвостка
140	мокрощелка
141	мудак
142	муде
143	мудеть
144	мудила
145	мудистый
146	мудня
147	мудоеб
148	мудозвон
149	муйня
150	нахуй
151	набздеть
152	наговнять
153	надристать
154	надрочить
155	наебал
156	наебаловка
157	наебать
158	наебка
159	наебнуться
160	наебывать
161	напиздеть
162	нассать
163	насцать
164	нахезать
165	нахуйник
166	обдристаться
167	обосранец
168	обосрать
169	обосцать
170	обосцаться
171	обсирать
172	опизде
173	опизденеть
174	отебукать
175	отпиздячить
176	отпороть
177	отхуевертить
178	отъебись
179	отъеть
180	охуевательский
181	охуевать
182	охуевающий
183	охуевший
184	охуеть
185	охуительный
186	охуячивать
187	охуячить
188	педрик
189	пердеж
190	пердение
191	пердеть
192	пердильник
193	перднуть
194	пердун
195	пердунец
196	пердунина
197	пердунья
198	пердуха
199	пердь
200	передок
201	пернуть
202	пидарас
203	пидор
204	пизда
205	пизданутый
206	пиздануть
207	пиздатый
208	пизденка
209	пизденыш
210	пиздеть
211	пиздец
212	пиздить
213	пиздища
214	пиздобратия
215	пиздоватый
216	пиздорванец
217	пиздорванка
218	пиздострадатель
219	пиздун
220	пиздюга
221	пиздюк
222	пиздячить
223	писять
224	питишка
225	плеха
226	подговнять
227	подзалупный
228	подъебнуться
229	поебать
230	поебустика
231	поеть
232	попысать
233	посрать
234	поставить
235	поцоватый
236	презерватив
237	припиздак
238	проститутка
239	похоть
240	проблядь
241	проебать
242	промандеть
243	промудеть
244	пропиздеть
245	пропиздячить
246	пысать
247	разъеба
248	разъебай
249	разъебанный
250	разъебать
251	распиздай
252	распиздеться
253	распиздяй
254	распроеть
255	растыка
256	сговнять
257	секель
258	серун
259	серька
260	сика
261	сикать
262	сикель
263	сила
264	сирать
265	сирывать
266	скурвиться
267	скуреха
268	скурея
269	скуряга
270	скуряжничать
271	спиздить
272	срака
273	сраный
274	сранье
275	срать
276	срун
277	ссака
278	ссаки
279	ссать
280	старпер
281	струк
282	сука
283	суходрочка
284	сучка
285	сцавинье
286	сцака
287	сцаки
288	сцание
289	сцать
290	сциха
291	сцуль
292	сцыха
293	сыкун
294	титечка
295	титечный
296	титка
297	титочка
298	титька
299	трахать
300	трипер
301	триппер
302	угондошить
303	уебан
304	уебать
305	уебок
306	уеть
307	усраться
308	усцаться
309	фик
310	фуй
311	хезать
312	хер
313	херня
314	херовина
315	херовый
316	хитровыебанный
317	хитрожопый
318	хлюха
319	хуевертить
320	хуевина
321	хуево
322	хуевый
323	хуеглот
324	хуек
325	хуепромышленник
326	хуерик
327	хуесос
328	хуета
329	хуеть
330	хуй
331	хуйня
332	хуйрик
333	хуистика
334	хуище
335	хуякать
336	хуякнуть
337	целка
338	членоплет
339	членосос
340	шлюха
\.


--
-- Data for Name: additional_entities_choice; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_choice (id, title, question_id) FROM stdin;
\.


--
-- Data for Name: additional_entities_city; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_city (id, city_name, coordinates, country_id) FROM stdin;
74	Белая Калитва	57.78567 36.693871	140
1	Абаза	52.651657 90.088572	140
2	Абакан	53.721152 91.442387	140
3	Абдулино	53.677839 53.647263	140
4	Абинск	44.866256 38.151163	140
5	Агидель	55.899835 53.92204	140
6	Агрыз	56.526318 52.995266	140
7	Адыгейск	44.884856 39.190567	140
8	Азнакаево	54.859808 53.074533	140
9	Азов	47.112442 39.423581	140
10	Ак-Довурак	51.178493 90.598474	140
11	Аксай	47.269804 39.862615	140
13	Алапаевск	57.853038 61.702672	140
14	Алатырь	54.839816 46.572195	140
15	Алдан	58.609451 125.381673	140
16	Алейск	52.492167 82.779448	140
17	Александров	56.397774 38.727621	140
18	Александровск	59.162925 57.584669	140
19	Александровск-Сахалинский	50.894564 142.1594	140
20	Алексеевка	50.629961 38.688095	140
21	Алексин	54.502429 37.066034	140
22	Алзамай	55.555072 98.664357	140
23	Альметьевск	54.901383 52.297113	140
24	Амурск	50.226797 136.910607	140
25	Анадырь	64.733115 177.508924	140
26	Анапа	44.894965 37.31617	140
27	Ангарск	52.544358 103.88824	140
28	Андреаполь	56.65079 32.262023	140
30	Анива	46.713168 142.526595	140
31	Апатиты	67.568041 33.407115	140
32	Апрелевка	55.545166 37.07322	140
33	Апшеронск	44.468327 39.736707	140
34	Аргун	56.694538 60.834315	140
35	Ардатов	54.84656 46.241183	140
36	Ардон	43.175598 44.295621	140
37	Арзамас	55.386666 43.815687	140
38	Аркадак	51.938814 43.499849	140
39	Армавир	44.997655 41.129644	140
40	Арсеньев	44.162084 133.269726	140
41	Арск	56.091311 49.876989	140
42	Артём	43.354804 132.18563	140
43	Артёмовск	54.347336 93.435749	140
44	Артёмовский	57.338402 61.894651	140
45	Архангельск	64.539393 40.516939	140
46	Асбест	57.005274 61.458114	140
47	Асино	56.997514 86.153906	140
48	Астрахань	46.347869 48.033574	140
49	Аткарск	51.873632 45.000296	140
50	Ахтубинск	48.284884 46.164413	140
51	Ачинск	56.269496 90.495231	140
52	Аша	54.990628 57.278469	140
53	Бабаево	59.389227 35.937759	140
54	Бабушкин	51.715833 105.864363	140
55	Бавлы	54.406333 53.245896	140
57	Байкальск	51.522821 104.149928	140
58	Баймак	52.591257 58.311199	140
59	Бакал	54.938064 58.809171	140
60	Баксан	43.681939 43.534613	140
61	Балабаново	55.177396 36.65677	140
62	Балаково	52.018424 47.819667	140
63	Балахна	56.504556 43.602005	140
64	Балашиха	55.796339 37.938199	140
65	Балашов	51.554601 43.146469	140
66	Балей	51.582284 116.637948	140
67	Балтийск	54.644072 19.892177	140
68	Барабинск	55.350412 78.341923	140
69	Барнаул	53.346785 83.776856	140
70	Барыш	53.653468 47.118029	140
71	Батайск	47.138333 39.744469	140
73	Бежецк	57.78567 36.693871	140
76	Белгород	50.59566 36.587223	140
77	Белебей	54.103441 54.111279	140
78	Белёв	53.809934 36.130097	140
79	Белинский	52.96562 43.408679	140
80	Белово	54.422114 86.303692	140
81	Белогорск	50.921287 128.473917	140
82	Белозерск	60.030843 37.789016	140
83	Белокуриха	51.99606 84.984004	140
85	Белорецк	53.967621 58.410023	140
86	Белореченск	44.761141 39.87114	140
87	Белоусово	55.089516 36.657812	140
88	Белоярский	63.716043 66.667588	140
89	Белый	55.83385 32.938805	140
90	Бердск	54.758288 83.107135	140
91	Березники	59.407922 56.804015	140
92	Берёзовский	56.910173 60.798203	140
93	Берёзовский	56.910173 60.798203	140
94	Беслан	43.19376 44.533792	140
95	Бийск	52.539297 85.21382	140
96	Бикин	46.818592 134.255034	140
97	Билибино	68.057129 166.451139	140
75	Белая Холуница	57.78567 36.693871	140
117	Большой Камень	53.443097 36.005087	140
138	Великие Луки	55.603969 31.197214	140
146	Верхний Тагил	53.876143 59.216953	140
148	Верхняя Пышма	53.876143 59.216953	140
147	Верхний Уфалей	53.876143 59.216953	140
192	Гаврилов Посад	55.205944 34.298037	140
191	Вятские Поляны	55.205944 34.298037	140
187	Вышний Волочёк	61.006355 36.449511	140
98	Биробиджан	48.794668 132.921754	140
99	Бирск	55.417531 55.530707	140
100	Бирюсинск	55.960876 97.820453	140
101	Бирюч	50.648389 38.400553	140
102	Благовещенск	50.28702 127.541025	140
103	Благовещенск	50.28702 127.541025	140
104	Благодарный	45.095649 43.440021	140
105	Бобров	51.097718 40.035604	140
106	Богданович	56.776502 62.046295	140
107	Богородицк	53.770694 38.131687	140
108	Богородск	56.103362 43.516755	140
109	Боготол	56.210117 89.531258	140
110	Богучар	49.935512 40.559079	140
111	Бокситогорск	59.473572 33.847675	140
112	Болгар	57.852118 114.198968	140
113	Бологое	57.885626 34.053776	140
114	Болотное	55.672001 84.385447	140
115	Болохово	54.082107 37.82679	140
116	Болхов	53.443097 36.005087	140
118	Бор	56.356517 44.064575	140
119	Борзя	50.387629 116.523485	140
121	Боровичи	58.388219 33.914025	140
122	Боровск	55.207634 36.483584	140
123	Бородино	55.905442 94.902177	140
124	Братск	56.151362 101.63408	140
125	Бронницы	55.425471 38.264108	140
126	Брянск	53.243562 34.363443	140
127	Бугульма	54.536413 52.789489	140
128	Бугуруслан	53.6523 52.432606	140
129	Будённовск	44.781528 44.165024	140
130	Бузулук	52.788116 52.262438	140
131	Буинск	54.964153 48.290142	140
132	Буй	58.481719 41.533113	140
133	Буйнакск	42.821749 47.115927	140
134	Бутурлиновка	50.835367 40.584825	140
135	Валдай	57.980199 33.246667	140
136	Валуйки	50.211194 38.099914	140
137	Велиж	55.603969 31.197214	140
141	Вельск	61.065915 42.10331	140
142	Венёв	54.350369 38.265527	140
144	Верея	55.343369 36.185694	140
145	Верхнеуральск	53.876143 59.216953	140
151	Верхотурье	58.862216 60.810213	140
152	Верхоянск	67.550161 133.390702	140
153	Весьегонск	58.658355 37.259019	140
154	Ветлуга	57.852885 45.776099	140
155	Видное	55.557174 37.708644	140
156	Вилюйск	63.751722 121.627326	140
157	Вилючинск	52.906857 158.418296	140
158	Вихоревка	56.120718 101.170396	140
159	Вичуга	57.217138 41.918149	140
160	Владивосток	43.115536 131.885485	140
161	Владикавказ	43.02115 44.68196	140
162	Владимир	56.129057 40.406635	140
163	Волгоград	48.707073 44.51693	140
164	Волгодонск	47.516545 42.198423	140
165	Волгореченск	57.439464 41.157456	140
166	Волжск	55.862267 48.372041	140
167	Волжский	56.053804 48.555271	140
168	Вологда	59.220496 39.891523	140
169	Володарск	56.21695 43.159729	140
171	Волосово	59.447275 29.48481	140
172	Волхов	59.916744 32.331544	140
173	Волчанск	59.934934 60.078796	140
174	Вольск	52.045978 47.38729	140
175	Воркута	67.49741 64.061091	140
176	Воронеж	51.660781 39.200269	140
177	Ворсма	55.98999 43.271955	140
178	Воскресенск	55.322978 38.673353	140
179	Воткинск	57.051806 53.987392	140
180	Всеволожск	60.021317 30.654084	140
181	Вуктыл	63.844407 57.29984	140
182	Выборг	60.710232 28.749404	140
183	Выкса	55.320683 42.167961	140
184	Высоковск	56.320243 36.551236	140
185	Высоцк	60.625264 28.568016	140
186	Вытегра	61.006355 36.449511	140
188	Вяземский	47.535352 134.755297	140
189	Вязники	56.247021 42.158862	140
190	Вязьма	55.205944 34.298037	140
140	Великий Устюг	55.603969 31.197214	140
193	Гаврилов-Ям	57.303309 39.849086	140
194	Гаджиево	69.249049 33.315262	140
195	Галич	58.381199 42.34749	140
196	Гатчина	59.568456 30.124473	140
197	Гвардейск	54.647708 21.071341	140
198	Гдов	58.744393 27.819585	140
199	Геленджик	44.561141 38.076809	140
200	Георгиевск	44.148599 43.473896	140
201	Глазов	58.14081 52.674235	140
202	Голицыно	55.615944 36.987117	140
203	Горбатов	56.130869 43.062701	140
204	Горно-Алтайск	51.958182 85.960373	140
205	Горнозаводск	58.374682 58.330917	140
206	Горняк	50.997775 81.464198	140
207	Городец	56.644822 43.472351	140
208	Городище	53.272758 45.70267	140
210	Гороховец	56.201695 42.691194	140
212	Грайворон	50.486223 35.666351	140
213	Гремячинск	58.562599 57.852034	140
214	Грозный	43.317776 45.694909	140
215	Грязи	52.496186 39.95533	140
216	Грязовец	58.875793 40.248423	140
217	Губаха	58.837018 57.554575	140
218	Губкин	51.283644 37.534748	140
219	Губкинский	51.18651 37.380687	140
220	Гудермес	43.35188 46.103535	140
221	Гуково	48.058442 39.940274	140
222	Гулькевичи	45.360342 40.695227	140
223	Гурьевск	54.285935 85.947635	140
224	Гурьевск	54.285935 85.947635	140
225	Гусев	54.591841 22.201117	140
226	Гусиноозёрск	51.285526 106.529323	140
227	Гусь-Хрустальный	55.619818 40.657902	140
228	Давлеканово	54.222727 55.03127	140
230	Далматово	56.258608 62.939311	140
231	Дальнегорск	44.554018 135.566179	140
233	Данилов	58.187861 40.174815	140
234	Данков	53.246197 39.134414	140
235	Дегтярск	56.698463 60.086674	140
236	Дедовск	55.859984 37.120669	140
237	Демидов	55.26444 31.515011	140
238	Дербент	42.057669 48.288776	140
239	Десногорск	54.152366 33.287872	140
240	Дзержинск	56.238377 43.461625	140
241	Дзержинский	55.630939 37.849616	140
242	Дивногорск	55.957721 92.380148	140
243	Дигора	43.156732 44.155035	140
244	Димитровград	54.217715 49.621984	140
245	Дмитриев	52.127774 35.080353	140
246	Дмитров	56.343942 37.520348	140
247	Дмитровск	52.505434 35.14151	140
248	Дно	57.826914 29.962992	140
249	Добрянка	58.468063 56.403986	140
250	Долгопрудный	55.933564 37.514104	140
251	Долинск	47.32624 142.79344	140
252	Донецк	48.015877 37.80285	140
253	Донской	47.992758 37.915058	140
254	Дорогобуж	54.912677 33.297035	140
255	Дрезна	55.741404 38.842371	140
256	Дубна	56.744002 37.173176	140
258	Дудинка	69.403081 86.190854	140
259	Духовщина	55.191351 32.414171	140
260	Дюртюли	55.48529 54.873463	140
261	Егорьевск	55.38305 39.035833	140
262	Ейск	46.711524 38.276451	140
263	Екатеринбург	56.838011 60.597465	140
264	Елабуга	55.75667 52.05446	140
265	Елец	52.62419 38.503653	140
266	Елизово	53.183053 158.388355	140
267	Ельня	54.575906 33.182734	140
268	Еманжелинск	54.752147 61.317223	140
269	Емва	62.598375 50.886569	140
270	Енисейск	58.453069 92.173769	140
271	Ермолино	55.197204 36.5952	140
272	Ершов	51.352068 48.283494	140
273	Ессентуки	44.044526 42.85891	140
274	Железноводск	44.132058 43.030533	140
275	Железногорск	52.337971 35.351743	140
277	Железногорск-Илимский	56.584843 104.114283	140
278	Жердевка	51.842282 41.461796	140
279	Жигулёвск	53.401714 49.494657	140
280	Жиздра	53.749114 34.734447	140
281	Жирновск	50.978713 44.778834	140
282	Жуков	55.03167 36.746503	140
283	Жуковка	53.533062 33.732547	140
284	Жуковский	53.498298 33.774598	140
285	Завитинск	50.106518 129.439309	140
286	Заводоуковск	56.508808 66.539174	140
287	Заволжск	57.491737 42.137491	140
229	Дагестанские Огни	54.222727 55.03127	140
288	Заволжье	56.640441 43.387164	140
289	Задонск	52.391972 38.919456	140
290	Заинск	55.298984 52.006391	140
291	Закаменск	50.372602 103.286764	140
292	Заозёрный	55.961818 94.709228	140
293	Заозёрск	69.400373 32.450139	140
295	Заполярный	69.426103 30.820739	140
296	Зарайск	54.756973 38.874845	140
297	Заречный	53.19611 45.169071	140
298	Заречный	53.19611 45.169071	140
299	Заринск	53.706332 84.931488	140
300	Звенигово	55.972312 48.01532	140
301	Звенигород	55.729686 36.855325	140
302	Зверево	55.499999 36.926211	140
303	Зеленогорск	56.113246 94.589006	140
304	Зеленоградск	54.95993 20.475354	140
305	Зеленодольск	55.846906 48.500617	140
307	Зерноград	46.849564 40.312815	140
308	Зея	53.734033 127.265889	140
309	Зима	53.92072 102.049065	140
310	Златоуст	55.172871 59.671841	140
311	Злынка	52.427384 31.737075	140
312	Змеиногорск	51.158015 82.18727	140
313	Знаменск	48.586634 45.736744	140
314	Зубцов	56.176143 34.58256	140
315	Зуевка	58.403217 51.133426	140
316	Ивангород	59.376655 28.223117	140
317	Иваново	57.000348 40.973921	140
318	Ивантеевка	55.971718 37.924338	140
319	Ивдель	60.697349 60.41729	140
320	Игарка	67.466954 86.567715	140
321	Ижевск	56.852593 53.204843	140
322	Избербаш	42.565141 47.871078	140
323	Изобильный	45.368536 41.708644	140
324	Иланский	56.238552 96.065297	140
325	Инза	53.857035 46.351649	140
326	Иннополис	55.75208 48.744609	140
327	Инсар	53.866508 44.372248	140
328	Инта	66.03682 60.115367	140
329	Ипатово	45.717419 42.911147	140
330	Ирбит	57.683819 63.057664	140
332	Исилькуль	54.911844 71.266945	140
333	Искитим	54.642582 83.306382	140
334	Истра	55.914287 36.860284	140
335	Ишим	56.11055 69.479639	140
336	Ишимбай	53.454621 56.04395	140
337	Йошкар-Ола	56.630842 47.886089	140
338	Кадников	59.503767 40.34404	140
339	Казань	55.796289 49.108795	140
340	Калач	50.424119 41.01624	140
341	Калач-на-Дону	48.681995 43.538234	140
342	Калачинск	55.052608 74.581782	140
343	Калининград	54.70739 20.507307	140
344	Калининск	51.499671 44.48548	140
345	Калтан	53.521083 87.27716	140
346	Калуга	54.513845 36.261215	140
347	Калязин	57.240412 37.855078	140
348	Камбарка	56.266057 54.193358	140
349	Каменка	53.185524 44.046896	140
351	Каменск-Уральский	56.414927 61.918708	140
352	Каменск-Шахтинский	48.320515 40.268923	140
353	Камень-на-Оби	53.791486 81.354558	140
354	Камешково	56.348916 40.995588	140
355	Камызяк	46.110571 48.073235	140
356	Камышин	50.083698 45.407367	140
357	Камышлов	56.846578 62.712288	140
358	Канаш	55.506943 47.491764	140
359	Кандалакша	67.151252 32.412823	140
360	Канск	56.205045 95.705055	140
361	Карабаново	56.313269 38.703438	140
362	Карабаш	55.490789 60.203042	140
363	Карабулак	43.305594 44.909404	140
364	Карасук	53.734294 78.042389	140
365	Карачаевск	43.773167 41.914313	140
366	Карачев	53.121594 34.982796	140
367	Каргат	55.194476 80.283039	140
368	Каргополь	61.505339 38.948166	140
369	Карпинск	59.766534 60.001227	140
370	Карталы	53.053681 60.647753	140
371	Касимов	54.937288 41.391368	140
372	Касли	55.893652 60.765918	140
373	Каспийск	42.890833 47.635674	140
375	Катайск	56.283235 62.58365	140
376	Качканар	58.70511 59.483959	140
377	Кашин	57.358381 37.61344	140
378	Кашира	54.834589 38.15154	140
379	Кедровый	57.560963 79.566965	140
380	Кемерово	55.354727 86.088374	140
381	Кемь	64.955532 34.598371	140
383	Кизел	59.049425 57.653875	140
294	Западная Двина	69.400373 32.450139	140
463	Красный Кут	56.010563 92.852572	140
384	Кизилюрт	43.204637 46.866878	140
385	Кизляр	43.84738 46.711685	140
386	Кимовск	53.972149 38.533063	140
387	Кимры	56.873338 37.355678	140
388	Кингисепп	59.374028 28.611297	140
389	Кинель	53.221004 50.634394	140
390	Кинешма	57.442544 42.168923	140
391	Киреевск	53.934944 37.928542	140
392	Киренск	57.775723 108.110816	140
393	Киржач	56.161709 38.872052	140
394	Кириллов	59.859059 38.374933	140
395	Кириши	59.449695 32.008707	140
396	Киров	58.603581 49.667978	140
397	Киров	58.603581 49.667978	140
398	Кировград	57.432415 60.062896	140
400	Кировск	67.612101 33.668165	140
401	Кировск	67.612101 33.668165	140
402	Кирс	59.339987 52.241516	140
403	Кирсанов	52.650646 42.728663	140
404	Киселёвск	54.006025 86.636679	140
405	Кисловодск	43.905225 42.716796	140
406	Клин	56.331693 36.728716	140
407	Клинцы	52.753143 32.233852	140
408	Княгинино	55.820566 45.032249	140
409	Ковдор	67.562914 30.474025	140
410	Ковылкино	54.039201 43.919056	140
411	Когалым	62.264069 74.482761	140
412	Кодинск	58.603398 99.179748	140
413	Козельск	54.034823 35.78226	140
414	Козловка	55.840386 48.245127	140
415	Козьмодемьянск	56.344167 46.568107	140
416	Кола	68.878636 33.026247	140
417	Кологрив	58.826929 44.318762	140
418	Коломна	55.103152 38.752917	140
419	Колпашево	58.311384 82.902679	140
420	Кольчугино	56.293901 39.376042	140
421	Коммунар	59.621609 30.393483	140
423	Комсомольск-на-Амуре	50.549923 137.007948	140
424	Конаково	56.713217 36.779309	140
425	Кондопога	62.20475 34.272758	140
426	Кондрово	54.80743 35.926647	140
427	Константиновск	47.577341 41.096694	140
428	Копейск	55.116732 61.61797	140
429	Кораблино	53.926812 40.034463	140
430	Кореновск	45.462742 39.448033	140
431	Коркино	54.892493 61.393049	140
432	Королёв	55.922212 37.854629	140
433	Короча	50.811036 37.194942	140
434	Корсаков	46.63498 142.78257	140
435	Коряжма	61.315335 47.159855	140
436	Костерёво	55.933701 39.624732	140
437	Костомукша	64.588014 30.598361	140
438	Кострома	57.767961 40.926858	140
439	Котельники	55.65984 37.863199	140
440	Котельниково	47.631528 43.142625	140
441	Котельнич	58.303426 48.347508	140
442	Котлас	61.25297 46.633217	140
443	Котово	50.322058 44.801319	140
444	Котовск	52.59292 41.50575	140
445	Кохма	56.932531 41.093208	140
447	Красноармейск	56.120959 38.14094	140
448	Красноармейск	56.120959 38.14094	140
449	Красновишерск	60.412821 57.083301	140
450	Красногорск	55.831099 37.330192	140
451	Краснодар	45.03547 38.975313	140
452	Краснозаводск	56.439338 38.245261	140
453	Краснознаменск	55.600506 37.042489	140
454	Краснознаменск	55.600506 37.042489	140
455	Краснокаменск	50.09372 118.033256	140
456	Краснокамск	58.078357 55.736376	140
457	Краснослободск	54.424901 43.784435	140
458	Краснослободск	54.424901 43.784435	140
459	Краснотурьинск	59.763761 60.193493	140
460	Красноуральск	58.35369 60.055961	140
461	Красноуфимск	56.617744 57.770692	140
462	Красноярск	56.010563 92.852572	140
466	Кремёнки	54.887036 37.116232	140
467	Кропоткин	45.434686 40.575994	140
468	Крымск	44.934986 37.986196	140
469	Кстово	56.15067 44.206751	140
471	Кувандык	51.478483 57.361168	140
472	Кувшиново	57.028957 34.165877	140
473	Кудрово	59.908489 30.513569	140
474	Кудымкар	59.014548 54.664183	140
475	Кузнецк	53.119335 46.601165	140
476	Куйбышев	53.195538 50.101783	140
477	Кукмор	56.186599 50.893981	140
464	Красный Сулин	56.010563 92.852572	140
542	Малая Вишера	55.205024 67.248601	140
519	Лодейное Поле	56.012269 37.474821	140
478	Кулебаки	55.429716 42.512483	140
479	Кумертау	52.756523 55.796976	140
480	Кунгур	57.42881 56.944206	140
481	Купино	54.366046 77.297254	140
482	Курган	55.441004 65.341118	140
483	Курганинск	44.887641 40.591364	140
484	Курильск	45.225174 147.883761	140
485	Курлово	55.454968 40.611208	140
486	Куровское	55.579144 38.920866	140
487	Курск	51.730361 36.192647	140
488	Куртамыш	54.912459 64.433505	140
489	Курчалой	43.20463 46.088955	140
490	Курчатов	51.660496 35.657143	140
491	Куса	55.338597 59.438603	140
492	Кушва	58.282566 59.764682	140
493	Кызыл	51.719086 94.437757	140
494	Кыштым	55.707877 60.538949	140
495	Кяхта	50.355214 106.449903	140
496	Лабинск	44.635387 40.724459	140
498	Лагань	45.392947 47.355202	140
499	Ладушкин	54.569116 20.172954	140
500	Лаишево	55.402449 49.543328	140
501	Лакинск	56.018001 39.956525	140
502	Лангепас	61.253701 75.180725	140
503	Лахденпохья	61.518857 30.199491	140
504	Лебедянь	53.020489 39.13135	140
505	Лениногорск	54.599028 52.442667	140
506	Ленинск	48.693682 45.199228	140
507	Ленинск-Кузнецкий	54.663609 86.162243	140
508	Ленск	60.713731 114.911844	140
509	Лермонтов	44.105344 42.973175	140
510	Лесозаводск	45.477955 133.418594	140
511	Лесосибирск	58.221728 92.503657	140
512	Ливны	52.426549 37.608041	140
513	Ликино-Дулёво	55.707786 38.957742	140
514	Липецк	52.60882 39.59922	140
515	Липки	53.94175 37.701915	140
516	Лиски	50.987298 39.497099	140
517	Лихославль	57.122219 35.466808	140
518	Лобня	56.012269 37.474821	140
521	Луга	58.735221 29.847999	140
522	Луза	60.629099 47.261229	140
523	Лукоянов	55.032697 44.493349	140
524	Луховицы	54.965217 39.025394	140
525	Лысково	56.021357 45.040962	140
526	Лысьва	58.100413 57.811655	140
527	Лыткарино	55.579297 37.908986	140
528	Льгов	51.656942 35.259432	140
529	Любань	52.798914 27.993481	140
530	Люберцы	55.676494 37.898116	140
531	Любим	58.362004 40.686873	140
532	Людиново	53.864607 34.447678	140
533	Лянтор	61.620663 72.155352	140
534	Магадан	59.568164 150.808541	140
535	Магас	43.171501 44.81624	140
536	Магнитогорск	53.407158 58.980282	140
537	Майкоп	44.608865 40.098548	140
538	Майский	44.605753 40.093069	140
539	Макаров	48.625101 142.778851	140
540	Макарьев	57.880009 43.807836	140
541	Макушино	55.205024 67.248601	140
543	Малгобек	43.509645 44.590188	140
544	Малмыж	56.524461 50.678232	140
546	Малоярославец	55.011897 36.462555	140
547	Мамадыш	55.717771 51.410224	140
548	Мамоново	54.463785 19.942267	140
549	Мантурово	58.328617 44.757292	140
550	Мариинск	56.206952 87.742263	140
552	Маркс	51.713333 46.740009	140
553	Махачкала	42.98306 47.504682	140
554	Мглин	53.061069 32.847806	140
555	Мегион	61.03289 76.102612	140
556	Медвежьегорск	62.914998 34.473101	140
557	Медногорск	51.403794 57.58324	140
558	Медынь	54.968784 35.857701	140
559	Межгорье	54.239989 57.961225	140
560	Междуреченск	53.686596 88.070372	140
561	Мезень	65.839904 44.25314	140
562	Меленки	55.338715 41.63403	140
563	Мелеуз	52.958964 55.92831	140
564	Менделеевск	55.895186 52.314397	140
565	Мензелинск	55.719972 53.101429	140
566	Мещовск	54.321476 35.278081	140
567	Миасс	55.045635 60.107731	140
568	Микунь	62.358008 50.071986	140
569	Миллерово	48.92173 40.394849	140
571	Минусинск	53.710564 91.687268	140
572	Миньяр	55.070912 57.548458	140
573	Мирный	62.541028 113.978692	140
632	Нижняя Салда	54.901233 99.026387	140
631	Нижний Тагил	54.901233 99.026387	140
629	Нижний Ломов	54.901233 99.026387	140
628	Нижние Серги	54.901233 99.026387	140
597	Набережные Челны	57.787134 38.455332	140
574	Мирный	62.541028 113.978692	140
575	Михайлов	54.232506 39.023508	140
576	Михайловка	50.070847 43.239723	140
577	Михайловск	45.129667 42.028803	140
578	Михайловск	45.129667 42.028803	140
579	Мичуринск	52.893913 40.498011	140
580	Могоча	53.736206 119.76608	140
581	Можайск	55.506714 36.017358	140
582	Можга	56.442802 52.213839	140
583	Моздок	43.735413 44.653878	140
584	Мончегорск	67.938931 32.937116	140
585	Морозовск	48.351157 41.830878	140
586	Моршанск	53.443611 41.811627	140
587	Мосальск	54.491307 34.984197	140
589	Муравленко	63.795285 74.494448	140
590	Мураши	59.3956 48.963851	140
591	Мурманск	68.970682 33.074981	140
592	Муром	55.579169 42.052411	140
593	Мценск	53.278939 36.575006	140
594	Мыски	53.712509 87.805747	140
595	Мытищи	55.910483 37.736402	140
596	Мышкин	57.787134 38.455332	140
598	Навашино	55.543888 42.18874	140
599	Наволоки	57.470588 41.957765	140
600	Надым	65.535924 72.531341	140
601	Назарово	56.012345 90.417688	140
602	Назрань	43.225727 44.764641	140
603	Называевск	55.567066 71.348718	140
604	Нальчик	43.485259 43.607072	140
605	Нариманов	46.690301 47.853623	140
606	Наро-Фоминск	55.38616 36.734493	140
607	Нарткала	43.556734 43.862022	140
608	Нарьян-Мар	67.63805 53.006926	140
609	Находка	42.824037 132.892811	140
610	Невель	56.02022 29.923969	140
612	Невинномысск	44.638287 41.936061	140
613	Невьянск	57.491225 60.218251	140
614	Нелидово	56.223296 32.776587	140
615	Неман	55.038836 22.028146	140
616	Нерехта	57.454414 40.572446	140
617	Нерчинск	51.95948 116.585415	140
618	Нерюнгри	56.659948 124.720315	140
619	Нестеров	54.631368 22.571357	140
620	Нефтегорск	52.797221 51.163799	140
621	Нефтекамск	56.088408 54.248236	140
622	Нефтекумск	44.750586 44.994088	140
623	Нефтеюганск	61.088212 72.616331	140
624	Нея	58.294389 43.878192	140
625	Нижневартовск	60.939716 76.569628	140
626	Нижнекамск	55.63407 51.809112	140
627	Нижнеудинск	54.901233 99.026387	140
634	Николаевск	50.025878 45.45911	140
636	Никольск	53.71447 46.084356	140
637	Никольск	53.71447 46.084356	140
638	Никольское	59.704642 30.788966	140
639	НоваяЛадога	59.704642 30.788966	140
640	НоваяЛяля	59.704642 30.788966	140
641	Новоалександровск	45.493304 41.215388	140
642	Новоалтайск	53.412021 83.93107	140
643	Новоаннинский	50.529658 42.66667	140
644	Нововоронеж	51.309213 39.216277	140
645	Новодвинск	64.413683 40.820821	140
646	Новозыбков	52.536717 31.933222	140
647	Новокубанск	45.103812 41.047493	140
648	Новокузнецк	53.757547 87.136044	140
649	Новокуйбышевск	53.099469 49.947767	140
650	Новомичуринск	54.034574 39.750865	140
651	Новомосковск	54.010993 38.290896	140
652	Новопавловск	43.957369 43.631901	140
653	Новоржев	57.029623 29.332419	140
654	Новороссийск	44.723912 37.768974	140
655	Новосибирск	55.030199 82.92043	140
656	Новосиль	52.974633 37.043756	140
657	Новосокольники	56.340749 30.152761	140
658	Новотроицк	51.196417 58.301767	140
659	Новоузенск	50.466326 48.132119	140
660	Новоульяновск	54.151718 48.384824	140
661	Новоуральск	57.247235 60.095604	140
663	Новочебоксарск	56.109551 47.479125	140
664	Новочеркасск	47.422052 40.093725	140
665	Новошахтинск	47.757738 39.93643	140
633	Нижняя Тура	54.901233 99.026387	140
713	Павловский Посад	59.686411 30.431598	140
668	Ногинск	55.854522 38.441831	140
669	Нолинск	57.559708 49.935712	140
670	Норильск	69.349033 88.201176	140
671	Ноябрьск	63.201801 75.450938	140
672	Нурлат	54.428117 50.804958	140
673	Нытва	57.939127 55.328622	140
674	Нюрба	63.278463 118.336617	140
675	Нягань	62.145759 65.433654	140
676	Нязепетровск	56.053673 59.609678	140
677	Няндома	61.669822 40.204388	140
678	Облучье	49.018898 131.053914	140
679	Обнинск	55.11201 36.586531	140
680	Обоянь	51.20995 36.26744	140
681	Обь	54.994594 82.693758	140
682	Одинцово	55.678859 37.263986	140
683	Озёрск	55.763184 60.707599	140
684	Озёрск	55.763184 60.707599	140
685	Озёры	54.854087 38.559824	140
686	Октябрьск	53.164038 48.670668	140
687	Октябрьский	54.481448 53.46557	140
688	Окуловка	58.377145 33.298679	140
689	Олёкминск	60.375796 120.406013	140
691	Олонец	60.979719 32.972034	140
692	Омск	54.989342 73.368212	140
693	Омутнинск	58.66406 52.177152	140
694	Онега	63.914485 38.086646	140
695	Опочка	56.714151 28.658881	140
696	Орёл	52.970371 36.063837	140
697	Оренбург	51.768199 55.096955	140
698	Орехово-Зуево	55.805837 38.981592	140
699	Орск	51.229362 58.475196	140
700	Оса	57.279672 55.468723	140
701	Осинники	53.598748 87.337069	140
702	Осташков	57.142872 33.115441	140
703	Остров	57.345188 28.343806	140
704	Островной	68.05439 39.514105	140
705	Острогожск	50.860139 39.082365	140
706	Отрадное	51.666104 39.33658	140
707	Отрадный	51.691727 39.21793	140
708	Оха	53.584521 142.947186	140
709	Оханск	57.72193 55.388656	140
710	Очёр	57.886894 54.715602	140
712	Павловск	59.686411 30.431598	140
714	Палласовка	50.050167 46.880398	140
715	Партизанск	43.119813 133.123246	140
716	Певек	69.701761 170.299935	140
717	Пенза	53.195063 45.018316	140
718	Первомайск	54.867632 43.801377	140
719	Первоуральск	56.905839 59.943249	140
720	Перевоз	55.596849 44.544931	140
721	Переславль-Залесский	56.736093 38.85431	140
722	Пермь	58.010374 56.229398	140
723	Пестово	58.599071 35.798098	140
724	ПетровВал	58.599071 35.798098	140
725	Петровск	52.314023 45.389931	140
727	Петрозаводск	61.785017 34.346878	140
728	Петропавловск-Камчатский	53.024075 158.643566	140
729	Петухово	55.065035 67.887375	140
730	Петушки	55.930967 39.4599	140
731	Печора	65.148602 57.223977	140
732	Печоры	57.813934 27.609064	140
733	Пикалёво	59.513113 34.177303	140
734	Пионерский	54.949482 20.224841	140
735	Питкяранта	61.573083 31.471254	140
736	Плавск	53.706843 37.291987	140
737	Плёс	57.460578 41.512254	140
738	Поворино	51.190773 42.245576	140
739	Подольск	55.431177 37.544737	140
740	Подпорожье	60.912784 34.156813	140
741	Покачи	61.742253 75.59412	140
742	Покров	55.916633 39.173374	140
743	Покровск	61.48424 129.148219	140
744	Полевской	56.446499 60.177072	140
745	Полесск	54.862777 21.109879	140
746	Полысаево	54.605443 86.280901	140
748	Полярный	69.198909 33.451033	140
749	Поронайск	49.22038 143.08956	140
750	Порхов	57.764855 29.553145	140
751	Похвистнево	53.653282 52.122346	140
752	Почеп	52.92913 33.454267	140
753	Починок	54.406265 32.439782	140
754	Пошехонье	58.503749 39.12005	140
755	Правдинск	54.44634 21.018817	140
756	Приволжск	57.380662 41.28083	140
757	Приморск	60.366014 28.613552	140
758	Приморск	60.366014 28.613552	140
760	Приозерск	61.036554 30.119838	140
761	Прокопьевск	53.884487 86.750055	140
666	Новый Оскол	47.757738 39.93643	140
762	Пролетарск	46.703849 41.727544	140
763	Протвино	54.870621 37.218316	140
764	Прохладный	43.758962 44.010083	140
765	Псков	57.81925 28.332065	140
766	Пугачёв	52.014871 48.795588	140
767	Пудож	61.80589 36.533	140
768	Пустошка	56.337526 29.36678	140
769	Пучеж	56.982087 43.168406	140
770	Пушкино	56.010428 37.847155	140
771	Пущино	54.832479 37.620977	140
772	Пыталово	57.063925 27.92396	140
773	Пыть-Ях	60.758589 72.836526	140
774	Пятигорск	44.03929 43.07084	140
775	Радужный	62.134265 77.458439	140
777	Райчихинск	49.794114 129.411255	140
778	Раменское	55.567326 38.22584	140
779	Рассказово	52.653842 41.874302	140
780	Ревда	56.800079 59.908718	140
781	Реж	57.373772 61.391639	140
782	Реутов	55.760515 37.855141	140
783	Ржев	56.262877 34.329065	140
784	Родники	57.107152 41.733366	140
785	Рославль	53.947309 32.85678	140
786	Россошь	50.192899 39.57652	140
787	Ростов-на-Дону	47.222078 39.720349	140
788	Ростов	47.222078 39.720349	140
789	Рошаль	55.663283 39.862759	140
790	Ртищево	52.257455 43.785657	140
791	Рубцовск	51.501207 81.2078	140
792	Рудня	54.947031 31.093576	140
793	Руза	55.701516 36.195997	140
794	Рузаевка	54.058268 44.94911	140
795	Рыбинск	58.048454 38.858406	140
796	Рыбное	54.730806 39.505463	140
798	Ряжск	53.708949 40.062894	140
799	Рязань	54.629216 39.736375	140
800	Салават	53.361651 55.924672	140
801	Салаир	54.235127 85.803007	140
802	Салехард	66.529844 66.614399	140
803	Сальск	46.475177 41.541135	140
804	Самара	53.195538 50.101783	140
805	Санкт-Петербург	59.939095 30.315868	140
806	Саранск	54.187433 45.183938	140
807	Сарапул	56.461621 53.803678	140
808	Саратов	51.533103 46.034158	140
809	Саров	54.922788 43.344844	140
810	Сасово	54.349928 41.924087	140
811	Сатка	55.040492 59.028881	140
812	Сафоново	55.106304 33.237917	140
813	Саяногорск	53.100762 91.412195	140
814	Саянск	53.139472 91.4792	140
815	Светлогорск	54.944006 20.151512	140
817	Светлый	54.67737 20.135719	140
818	Светогорск	61.111193 28.87268	140
819	Свирск	53.066567 103.342244	140
820	Свободный	51.375889 128.134147	140
821	Себеж	56.277398 28.484814	140
822	Северо-Курильск	50.676327 156.124106	140
823	Северобайкальск	55.635996 109.335597	140
824	Северодвинск	64.562501 39.818175	140
825	Североморск	69.076153 33.416215	140
826	Североуральск	60.153281 59.952556	140
827	Северск	56.603185 84.880913	140
828	Севск	52.156089 34.495091	140
829	Сегежа	63.743701 34.312617	140
830	Сельцо	53.373933 34.105932	140
831	Семёнов	56.789012 44.490331	140
832	Семикаракорск	47.517792 40.811505	140
833	Семилуки	51.695255 39.018953	140
834	Сенгилей	53.96207 48.790584	140
835	Серафимович	49.584135 42.734008	140
836	Сергач	55.520105 45.481361	140
838	Сердобск	52.455683 44.202735	140
839	Серпухов	54.913536 37.416763	140
840	Сертолово	60.141613 30.211879	140
841	Сибай	52.72051 58.666429	140
842	Сим	54.990716 57.689969	140
844	Скопин	53.82359 39.549328	140
845	Славгород	52.999375 78.64594	140
846	Славск	55.043819 21.680067	140
847	Славянск-на-Кубани	45.260439 38.126001	140
848	Сланцы	59.11779 28.088136	140
849	Слободской	58.731886 50.183674	140
850	Слюдянка	51.656501 103.718845	140
851	Смоленск	54.782635 32.045251	140
852	Снежинск	56.085209 60.732536	140
853	Снежногорск	69.192168 33.238303	140
854	Собинка	55.993837 40.017943	140
855	Советск	57.587599 48.959521	140
856	Советск	57.587599 48.959521	140
857	Советск	57.587599 48.959521	140
858	Советская Гавань	57.587599 48.959521	140
884	Старая Купавна	45.044521 41.969083	140
885	Старая Русса	45.044521 41.969083	140
889	Старый Оскол	52.585277 32.760346	140
859	Сокол	59.460968 40.099977	140
860	Солигалич	59.07858 42.287815	140
861	Соликамск	59.648333 56.771029	140
863	Соль-Илецк	51.16185 54.980336	140
864	Сольвычегодск	61.330589 46.928089	140
865	Сольцы	58.120168 30.309355	140
866	Сорочинск	52.429092 53.151016	140
867	Сорск	54.002606 90.253323	140
868	Сортавала	61.703306 30.691723	140
869	Сосенский	54.059489 35.966038	140
870	Сосновка	56.253352 51.283364	140
871	Сосновоборск	56.120211 93.335434	140
873	Сосногорск	63.59911 53.876441	140
874	Сочи	43.585525 39.723062	140
875	Спас-Деменск	54.409834 34.018948	140
876	Спас-Клепики	55.131038 40.175786	140
877	Спасск	53.926494 43.187729	140
878	Спасск-Дальний	44.597641 132.817559	140
879	Спасск-Рязанский	54.407072 40.376424	140
880	Среднеколымск	67.458183 153.707009	140
881	Среднеуральск	56.991837 60.477136	140
882	Сретенск	52.246252 117.71192	140
883	Ставрополь	45.044521 41.969083	140
886	Старица	56.514927 34.933586	140
887	Стародуб	52.585277 32.760346	140
891	Стрежевой	60.732862 77.604002	140
892	Струнино	56.37493 38.584079	140
893	Ступино	54.88688 38.07839	140
894	Суворов	54.122083 36.490339	140
895	Суджа	51.190953 35.268918	140
896	Судогда	55.949879 40.856295	140
897	Суздаль	56.419836 40.449457	140
898	Сунжа	43.320353 45.047682	140
899	Суоярви	62.087896 32.373738	140
900	Сураж	53.013891 32.393043	140
901	Сургут	61.254035 73.396221	140
902	Суровикино	48.605493 42.844195	140
903	Сурск	53.07604 45.6911	140
904	Сусуман	62.780464 148.153687	140
905	Сухиничи	54.101752 35.339319	140
906	СухойЛог	54.101752 35.339319	140
907	Сызрань	53.155782 48.474485	140
908	Сыктывкар	61.668793 50.836399	140
909	Сысерть	56.502281 60.810025	140
910	Сычёвка	55.83161 34.277834	140
911	Сясьстрой	60.141954 32.556743	140
912	Тавда	58.041871 65.272595	140
913	Таганрог	47.220983 38.9173	140
914	Тайга	56.065138 85.631024	140
916	Талдом	56.73084 37.527633	140
917	Талица	56.595192 37.661689	140
918	Тамбов	52.721219 41.452274	140
919	Тарко-Сале	64.911819 77.761055	140
920	Таруса	54.729122 37.17959	140
921	Татарск	55.214532 75.97409	140
922	Таштагол	52.763912 87.848309	140
923	Тверь	56.859611 35.911896	140
924	Теберда	43.443841 41.741423	140
925	Тейково	56.85436 40.535471	140
926	Темников	54.630967 43.216089	140
927	Темрюк	45.27841 37.370194	140
928	Терек	43.483865 44.140267	140
929	Тетюши	54.936931 48.830074	140
930	Тимашёвск	45.61478 38.934332	140
931	Тихвин	59.644209 33.542096	140
932	Тихорецк	45.85468 40.125929	140
933	Тобольск	58.201698 68.253762	140
934	Тогучин	55.238013 84.402865	140
936	Томари	47.762214 142.061627	140
937	Томмот	58.958666 126.287579	140
938	Томск	56.48464 84.947649	140
939	Топки	55.276508 85.615223	140
940	Торжок	57.041338 34.96014	140
941	Торопец	56.501173 31.635466	140
942	Тосно	59.540664 30.877719	140
943	Тотьма	59.973487 42.758873	140
944	Трёхгорный	54.817842 58.446423	140
945	Троицк	54.083217 61.559759	140
946	Трубчевск	52.579077 33.766073	140
947	Туапсе	44.09564 39.073553	140
948	Туймазы	54.599988 53.695008	140
949	Тула	54.193122 37.617348	140
950	Туран	52.144916 93.917309	140
951	Туринск	58.039442 63.698144	140
952	Тутаев	57.8688 39.530759	140
953	Тында	55.154656 124.729236	140
954	Тырныауз	43.398084 42.921423	140
955	Тюкалинск	55.870506 72.195506	140
956	Тюмень	57.153033 65.534328	140
957	Уварово	51.983099 42.261	140
958	Углегорск	49.081575 142.069281	140
959	Углич	57.526592 38.319372	140
960	Удачный	66.406995 112.306362	140
961	Удомля	57.876779 35.00511	140
962	Ужур	55.320155 89.844006	140
963	Узловая	53.97844 38.160299	140
964	Улан-Удэ	51.834464 107.584574	140
965	Ульяновск	54.314192 48.403123	140
966	Унеча	52.845115 32.670676	140
967	Урай	60.129632 64.803944	140
968	Урень	57.463042 45.799527	140
969	Уржум	57.109738 50.005717	140
971	Урюпинск	50.794522 41.995844	140
972	Усинск	65.994144 57.55701	140
973	Усмань	52.043386 39.736069	140
974	Усолье-Сибирское	52.756648 103.638769	140
975	Усолье	52.756648 103.638769	140
976	Уссурийск	43.797273 131.95178	140
977	Усть-Джегута	44.083895 41.971042	140
978	Усть-Илимск	54.55712 100.578038	140
979	Усть-Катав	54.930289 58.1747	140
980	Усть-Кут	56.792838 105.775699	140
981	Усть-Лабинск	45.213625 39.691234	140
982	Устюжна	58.838391 36.442414	140
983	Уфа	54.735147 55.958727	140
984	Ухта	63.562626 53.684022	140
985	Учалы	54.319176 59.378631	140
986	Уяр	55.813172 94.328297	140
987	Фатеж	52.091789 35.853892	140
988	Фокино	53.455436 34.415923	140
989	Фокино	53.455436 34.415923	140
990	Фролово	49.765861 43.649292	140
991	Фрязино	55.957938 38.052339	140
992	Фурманов	57.252601 41.106189	140
993	Хабаровск	48.480223 135.071917	140
995	Ханты-Мансийск	61.00318 69.018902	140
996	Харабали	47.409315 47.252058	140
997	Харовск	59.95074 40.20631	140
998	Хасавюрт	43.246265 46.590044	140
999	Хвалынск	52.495501 48.105772	140
1000	Хилок	51.363401 110.459012	140
1001	Химки	55.88874 37.43039	140
1002	Холм	57.145202 31.178781	140
1003	Холмск	47.040905 142.041622	140
1004	Хотьково	56.252182 37.978677	140
1005	Цивильск	55.86501 47.47298	140
1006	Цимлянск	47.647714 42.09306	140
1007	Чадан	51.284472 91.578913	140
1008	Чайковский	56.778061 54.147759	140
1009	Чапаевск	52.981709 49.710217	140
1010	Чаплыгин	53.240555 39.96699	140
1011	Чебаркуль	54.977785 60.37012	140
1012	Чебоксары	56.146277 47.251079	140
1013	Чегем	43.567114 43.586626	140
1014	Чекалин	54.098505 36.247372	140
1016	Чердынь	60.402836 56.479543	140
1017	Черемхово	53.136911 103.090096	140
1018	Черепаново	54.228417 83.372201	140
1019	Череповец	59.122612 37.903461	140
1020	Черкесск	44.226863 42.04677	140
1021	Чёрмоз	58.784335 56.150796	140
1022	Черноголовка	56.010005 38.379245	140
1023	Черногорск	53.827013 91.306005	140
1024	Чернушка	56.51601 56.076361	140
1025	Черняховск	54.630706 21.819503	140
1026	Чехов	55.149851 37.466997	140
1027	Чистополь	55.372334 50.643575	140
1028	Чита	52.033973 113.499432	140
1029	Чкаловск	56.766253 43.251105	140
1030	Чудово	59.12119 31.670285	140
1031	Чулым	55.091258 80.963288	140
1032	Чусовой	58.297548 57.819318	140
1033	Чухлома	58.753399 42.688526	140
1034	Шагонар	51.534705 92.919972	140
1035	Шадринск	56.087042 63.629747	140
1036	Шали	43.1488 45.900991	140
1038	Шарья	58.369849 45.518264	140
1039	Шахты	47.709601 40.215797	140
1040	Шахунья	57.676379 46.612915	140
1041	Шацк	51.496839 23.930185	140
1042	Шебекино	50.400498 36.887916	140
1043	Шелехов	52.210209 104.097395	140
1044	Шенкурск	62.10565 42.899612	140
1045	Шимановск	51.85262 116.032735	140
1046	Шиханы	52.114774 47.202327	140
1047	Шлиссельбург	59.934943 31.026597	140
1048	Шумерля	55.497934 46.417846	140
1049	Шумиха	55.228726 63.28571	140
1050	Шуя	56.852037 41.385556	140
1051	Щёкино	54.002146 37.517626	140
150	Верхняя Тура	53.876143 59.216953	140
1053	Щёлково	55.920209 37.991478	140
1054	Щигры	51.87619 36.912	140
1055	Щучье	55.208831 62.747853	140
1056	Электрогорск	55.883161 38.786209	140
1057	Электросталь	55.784445 38.444849	140
1058	Электроугли	55.716859 38.219659	140
1059	Элиста	46.307743 44.269759	140
1060	Энгельс	51.485489 46.126783	140
1061	Эртиль	51.835727 40.799243	140
1062	Югорск	61.314917 63.331964	140
1063	Южа	56.583698 42.011843	140
1064	Южно-Сахалинск	46.959155 142.738023	140
1065	Южно-Сухокумск	44.660166 45.649966	140
1066	Южноуральск	54.442455 61.268229	140
1067	Юрга	55.713557 84.933869	140
1068	Юрьев-Польский	56.49925 39.680814	140
1069	Юрьевец	57.317815 43.110995	140
1070	Юрюзань	54.854646 58.422662	140
1071	Юхнов	54.744201 35.238878	140
1072	Ядрин	55.940689 46.202107	140
1073	Якутск	62.028103 129.732663	140
1074	Ялуторовск	56.654689 66.312206	140
1075	Янаул	56.264957 54.929824	140
1076	Яранск	57.304228 47.885855	140
1077	Яровое	52.923446 78.569601	140
1078	Ярославль	57.626569 39.893787	140
1079	Ярцево	57.535951 40.006121	140
1080	Ясногорск	54.479555 37.689689	140
1081	Ясный	51.036877 59.874349	140
1082	Яхрома	56.28989 37.483858	140
1052	Щёлкино Оспаривается	45.428886 35.825065	140
72	Бахчисарай	44.754887 33.85214	140
149	Верхняя Салда	53.876143 59.216953	140
211	Горячий Ключ	56.201695 42.691194	140
465	Красный Холм	56.010563 92.852572	140
570	Минеральные Воды	48.92173 40.394849	140
630	Нижний Новгород	54.901233 99.026387	140
667	Новый Уренгой	47.757738 39.93643	140
747	Полярные Зори	54.605443 86.280901	140
837	Сергиев Посад	55.520105 45.481361	140
1083	Антополь	52.2041343 24.7853018	15
1085	Белоозерск	52.4717355 25.1783133	15
1086	Береза	52.5373125 24.9788566	15
1087	Береза Картуска	0 0	15
1088	Брест	52.0976214 23.7340503	15
1089	Высокое	52.367978 23.3759718	15
1090	Ганцевичи	52.7634482 26.4275001	15
1091	Городище	53.3269782 26.0063136	15
1092	Давид-Городок	52.0546671 27.2119237	15
1093	Домачево	51.7441207 23.5951587	15
1094	Дрогичин	52.1930413 25.1471719	15
1095	Жабинка	52.1954738 24.014935	15
1096	Иваново	52.145887 25.5329454	15
1097	Ивацевичи	52.7085795 25.3346543	15
1098	Каменец	52.3979454 23.8257811	15
1099	Кобрин	52.2141109 24.3581792	15
1100	Коссово	52.7567887 25.1531057	15
1101	Лунинец	52.2513941 26.8066432	15
1102	Ляховичи	53.0399358 26.2614947	15
1103	Малорита	51.7925615 24.0739629	15
1104	Микашевичи	52.2160531 27.4751997	15
1105	Пинск	52.1124967 26.0634602	15
1106	Пружаны	52.5557638 24.4554645	15
1107	Столин	51.8873063 26.8394148	15
1109	Бегомль	54.7318321 28.0605962	15
1110	Бешенковичи	55.0444134 29.4559263	15
1111	Богушевск	54.8420473 30.2064824	15
1112	Браслав	55.6411645 27.0450814	15
1113	Верхнедвинск	55.7784607 27.9323817	15
1114	Ветрино	55.4104842 28.4633425	15
1115	Видзы	55.3948269 26.6327297	15
1116	Витебск	55.1848061 30.201622	15
1117	Воропаево	55.1390249 27.2066843	15
1118	Глубокое	55.1391321 27.6842904	15
1119	Городок	55.4618616 29.9874438	15
1120	Дисна	55.5662814 28.2137745	15
1121	Докшицы	54.8953858 27.7599272	15
1122	Друя	55.7859618 27.4327467	15
1123	Дубровно	54.5734035 30.6828298	15
1124	Езерище	55.8384089 29.9937851	15
1125	Лепель	54.878179 28.6980563	15
1126	Лиозно	55.024145 30.8005553	15
1127	Миоры	55.6226563 27.633435	15
1129	Новополоцк	55.5146432 28.5606439	15
1130	Орша	54.5071478 30.4119546	15
1131	Полоцк	55.4831573 28.7990619	15
1132	Поставы	55.1134117 26.8433286	15
1133	Россоны	55.9014488 28.8200362	15
1135	Толочин	54.4098787 29.6935064	15
1136	Ушачи	55.1786995 28.6159394	15
1137	Чашники	54.847813 29.1730691	15
1138	Шарковщина	55.3682716 27.4703402	15
1139	Шумилино	55.3000777 29.6112895	15
1140	Белицк	52.9382677 30.4114864	15
1141	Большевик	52.5645365 30.8769586	15
1142	Брагин	51.7954009 30.2688788	15
1143	Буда-Кошелево	52.7201592 30.569225	15
1144	Василевичи	52.2443711 29.8315009	15
1145	Васильевка	52.2449975 31.5048893	15
1146	Ветка	52.5662086 31.1730798	15
1147	Гомель	52.4411761 30.9878462	15
1148	Добруш	52.4031652 31.3294618	15
1149	Ельск	51.8137357 29.1596054	15
1151	Жлобин	52.8888952 30.0282481	15
1152	Калинковичи	52.1253899 29.3297633	15
1153	Корма	53.1307962 30.7935909	15
1154	Лельчицы	51.7959101 28.3296165	15
1155	Лоев	51.9377873 30.7892014	15
1156	Мозырь	52.0322082 29.2223129	15
1157	Наровля	51.8010382 29.4967759	15
1158	Октябрьский	52.6473109 28.8851644	15
1159	Петриков	52.1267722 28.4919521	15
1160	Речица	52.3635403 30.3923965	15
1161	Рогачев	53.0918554 30.0503982	15
1162	Светлогорск	52.6266995 29.7490257	15
1163	Туров	52.0663389 27.7405067	15
1164	Хойники	51.9109552 29.9994415	15
1165	Чечерск	52.9186475 30.91628	15
1166	Берёзовка	53.7221715 25.5004738	15
1167	Большая Берестовица	53.1948656 24.0191604	15
1168	Волковыск	53.1516417 24.4422029	15
1169	Вороново	54.1499032 25.3160274	15
1170	Гродно	53.6693538 23.8131306	15
1171	Дятлово	53.4651358 25.4074899	15
1172	Желудок	53.5977548 24.9840659	15
1173	Зельва	53.1501463 24.8029785	15
1174	Ивье	53.9323017 25.777486	15
1176	Кореличи	53.5666638 26.1406893	15
1177	Лида	53.8873843 25.2894383	15
1178	Мосты	53.4102363 24.5338654	15
1179	Новогрудок	53.597736 25.8243706	15
1180	Островец	54.6105209 25.9524709	15
1181	Ошмяны	54.4243464 25.9351597	15
1182	Свислочь	53.0358086 24.0942728	15
1183	Скидель	53.5866599 24.2503492	15
1184	Слоним	53.0875127 25.3087192	15
1185	Сморгонь	54.4762327 26.3981493	15
1186	Щучин	53.6040518 24.741899	15
1187	Березино	53.8446885 28.9892933	15
1188	Бобр	54.3404541 29.2745787	15
1189	Борисов	54.2144309 28.508436	15
1190	Вилейка	54.4980119 26.9200749	15
1191	Воложин	54.0878914 26.533109	15
1192	Городея	53.3118876 26.529787	15
1193	Дзержинск	53.6849853 27.1325559	15
1194	Жодино	54.1016136 28.3471258	15
1195	Заславль	54.0006143 27.276841	15
1197	Ивенец	53.8882122 26.7405467	15
1198	Клецк	53.0637214 26.6392615	15
1199	Копыль	53.1511461 27.0908004	15
1200	Крупки	54.3269605 29.1426031	15
1201	Логойск	54.2042169 27.8532022	15
1202	Любань	52.7990255 27.9918895	15
1203	Марьина горка	53.506761 28.1527803	15
1204	Минск	53.9045398 27.5615244	15
1205	Молодечно	54.3104099 26.8488824	15
1206	Мядель	54.8771794 26.9388432	15
1207	Несвиж	53.2226038 26.6766138	15
1208	Пуховичи	53.5339049 28.2501616	15
1209	Раков	53.9667658 27.0469131	15
1210	Руденск	53.5977081 27.8611129	15
1211	Слуцк	53.0210495 27.5540131	15
1212	Смолевичи	54.0297214 28.0892299	15
1213	Солигорск	52.7899466 27.5359618	15
1214	Старые дороги	53.0389897 28.2605496	15
1215	Столбцы	53.4862776 26.7452131	15
1216	Узда	53.4619521 27.215089	15
1217	Фаниполь	53.746238 27.3375641	15
1218	Червень	53.7117479 28.4244728	15
1219	Асеньковичи	0 0	15
1220	Белыничи	53.9969111 29.707695	15
1222	Быхов	53.5180441 30.2402914	15
1223	Глуск	52.8996249 28.6709271	15
1224	Глуша	53.0864876 28.856285	15
1225	Горки	54.2825201 30.990449	15
1226	Гродзянка	53.5488048 28.7434739	15
1227	Елизово	53.3975307 29.0037835	15
1228	Дрибин	54.1190657 31.1014303	15
12	Алагир	43.041711 44.219875	140
29	Анжеро-Судженск	56.083175 86.018216	140
56	Багратионовск	54.386509 20.639638	140
84	Беломорск	64.53032 34.763328	140
120	Борисоглебск	51.367725 42.074977	140
143	Верещагино	58.079761 54.658083	140
170	Волоколамск	56.035728 35.958537	140
139	Великий Новгород	55.603969 31.197214	140
209	Городовиковск	46.083105 41.936052	140
232	Дальнереченск	45.93085 133.731738	140
257	Дубовка	49.055369 44.826957	140
276	Железногорск	52.337971 35.351743	140
306	Зеленокумск	44.403288 43.884148	140
331	Иркутск	52.287054 104.281047	140
350	Каменногорск	60.95081 29.130882	140
374	Катав-Ивановск	54.752074 58.198443	140
399	Кирово-Чепецк	58.556581 50.043932	140
422	Комсомольск	57.027394 40.37761	140
446	Красавино	60.961377 46.481474	140
470	Кубинка	55.575556 36.695209	140
497	Лабытнанги	66.660595 66.383963	140
520	Лосино-Петровский	55.87137 38.200606	140
545	Малоархангельск	52.400974 36.502107	140
551	Мариинский Посад	56.206952 87.742263	140
588	Москва	55.753215 37.622504	140
611	Невельск	46.652828 141.863126	140
635	Николаевск-на-Амуре	53.146143 140.711046	140
662	Новохопёрск	51.100286 41.631452	140
690	Оленегорск	68.142161 33.26696	140
711	Павлово	55.964629 43.06457	140
726	Петровск-Забайкальский	51.274889 108.846689	140
759	Приморско-Ахтарск	46.043502 38.177645	140
776	Радужный	62.134265 77.458439	140
797	Рыльск	51.571431 34.683288	140
816	Светлоград	45.328573 42.856628	140
843	Сковородино	53.987177 123.943632	140
862	Солнечногорск	56.185102 36.977631	140
890	Стерлитамак	53.630403 55.930825	140
915	Тайшет	55.940502 98.002982	140
935	Тольятти	53.508816 49.419207	140
872	Сосновый Бор	56.120211 93.335434	140
970	Урус-Мартан	43.127617 45.540614	140
994	Хадыженск	44.422804 39.537326	140
1015	Челябинск	55.159897 61.402554	140
1037	Шарыпово	55.539064 89.180151	140
1084	Барановичи	53.1255737 26.0091683	15
1108	Барань	54.4788881 30.3160067	15
1128	Новолукомль	54.6575917 29.1509792	15
1134	Сенно	54.8133814 29.7063314	15
1150	Житковичи	52.2160819 27.8502774	15
1175	Козловщина	53.3190638 25.2873294	15
1196	Зеленый Бор	54.0164763 28.4864947	15
1221	Бобруйск	53.1446069 29.2213753	15
1229	Кировск	53.2691975 29.4765176	15
1230	Климовичи	53.6091856 31.9594674	15
1231	Кличев	53.4917756 29.3327583	15
1232	Костюковичи	53.3449659 32.0532332	15
1233	Краснополье	53.3383537 31.3972255	15
1234	Кричев	53.7093085 31.7171895	15
1235	Круглое	54.2483092 29.796286	15
1236	Могилев	53.9007159 30.3313598	15
1237	Мстиславль	54.0188307 31.7244374	15
1238	Осиповичи	53.3048792 28.6357281	15
1239	Славгород	53.4431223 30.9995629	15
1240	Хотимск	53.4099308 32.5773652	15
1241	Чаусы	53.8017532 30.953397	15
1242	Чериков	53.569694 31.37973	15
1243	Шклов	54.2023958 30.2955436	15
\.


--
-- Data for Name: additional_entities_country; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_country (id, name_country) FROM stdin;
1	Австралия
2	Австрия
3	Азербайджан
4	Албания
5	Ангола
6	Андорра
7	Аргентина
8	Армения
9	Аруба
10	Афганистан
11	Багамские Острова
12	Бангладеш
13	Барбадос
14	Бахрейн
15	Беларусь
16	Бельгия
17	Бенин
18	Бермудские Острова
19	Болгария
20	Боливия
21	Босния и Герцеговина
22	Ботсвана
23	Бразилия
24	Бруней
25	Буркина - Фасо
26	Бурунди
27	Бутан
28	Ватикан
29	Великобритания
30	Венгрия
31	Венесуэла
32	Виргинские Острова
33	Восточный Тимор
34	Вьетнам
35	Габон
36	Гаити
37	Гайана
38	Гамбия
39	Гана
40	Гваделупа
41	Гватемала
42	Гвинея
43	Гвинея-Бисау
44	Германия
45	Гибралтар
46	Гондурас
47	Гонконг
48	Гренада
49	Гренландия
50	Греция
51	Грузия
52	Дания
53	Демократическая Республика Конго
54	Доминика
55	Египет
56	Замбия
57	Зимбабве
58	Израиль
59	Индия
60	Индонезия
61	Иордания
62	Ирак
63	Иран
64	Ирландия
65	Исландия
66	Испания
67	Италия
68	Йемен
69	Кабо - Верде
70	Казахстан
71	Каймановы острова
72	Камбоджа
73	Камерун
74	Канада
75	Катар
76	Кения
77	Кипр
78	Киргизия
79	Китай
80	Кокосовые острова
81	Колумбия
82	Коморы
83	Косово
84	Коста - Рика
85	Кот-д'Ивуар
86	Куба
87	Кувейт
88	Лаос
89	Латвия
90	Лесото
91	Либерия
92	Ливан
93	Ливия
94	Литва
95	Лихтенштейн
96	Люксембург
97	Маврикий
98	Мавритания
99	Мадагаскар
100	Майотта
101	Макао
102	Македония
103	Малави
104	Малайзия
105	Мали
106	Мальдивы
107	Мальта
108	Марокко
109	Мартиника
110	Маршалловы Острова
111	Мексика
112	Микронезия
113	Мозамбик
114	Молдова
115	Монако
116	Монголия
117	Мьянма
118	Намибия
119	Непал
120	Нигер
121	Нигерия
122	Нидерланды
123	Никарагуа
124	Новая Зеландия
125	Новая Каледония
126	Норвегия
127	Объединенные Арабские Эмираты
128	Оман
129	Остров Мэн
130	Пакистан
131	Палау
132	Панама
133	Папуа - Новая Гвинея
134	Парагвай
135	Перу
136	Польша
137	Португалия
138	Пуэрто-Рико
139	Республика Конго
140	Россия
141	Руанда
142	Румыния
143	Сальвадор
144	Самоа
145	Сан-Марино
146	Саудовская Аравия
147	Северная Корея
148	Сейшельские Острова
149	Сенегал
150	Сербия
151	Сингапур
152	Сирия
153	Словакия
154	Словения
155	США
156	Соломоновы Острова
157	Сомали
158	Судан
159	Суринам
160	Сьерра - Леоне
161	Таджикистан
162	Таиланд
163	Тайвань
164	Танзания
165	Того
166	Токелау
167	Тонга
168	Тринидад и Тобаго
169	Тунис
170	Туркменистан
171	Турция
172	Уганда
173	Узбекистан
174	Украина
175	Уругвай
176	Фарерские острова
177	Фиджи
178	Филиппины
179	Финляндия
180	Фолклендские острова
181	Франция
182	Хорватия
183	ЦАР
184	Чад
185	Черногория
186	Чехия
187	Чили
188	Швейцария
189	Швеция
190	Шпицберген
191	Шри - Ланка
192	Эквадор
193	Экваториальная Гвинея
194	Эритрея
195	Эстония
196	Эфиопия
197	Южная Африка
198	Южная Корея
199	Южный Судан
200	Ямайка
201	Ян - Майен
202	Япония
\.


--
-- Data for Name: additional_entities_customsettings; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_customsettings (id, distance_for_unique_places, days_request_to_not_auth_user) FROM stdin;
1	100	1
\.


--
-- Data for Name: additional_entities_emailfragment; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_emailfragment (id, verify_email, reset_password, verify_email_for_not_auth_request) FROM stdin;
1	Для верификации Вашей электронной почты, необходимо перейти по ссылке:	Для восстановление Вашего пароля, необходимо перейти по ссылке:	\N
\.


--
-- Data for Name: additional_entities_language; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_language (id, name_language) FROM stdin;
1	русский
2	english
3	français
4	español
5	deutsch
6	italiano
\.


--
-- Data for Name: additional_entities_question; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.additional_entities_question (id, title, is_hide) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add pro category	7	add_procategory
26	Can change pro category	7	change_procategory
27	Can delete pro category	7	delete_procategory
28	Can view pro category	7	view_procategory
29	Can add profile	8	add_profile
30	Can change profile	8	change_profile
31	Can delete profile	8	delete_profile
32	Can view profile	8	view_profile
33	Can add specialization	9	add_specialization
34	Can change specialization	9	change_specialization
35	Can delete specialization	9	delete_specialization
36	Can view specialization	9	view_specialization
37	Can add verification code	10	add_verificationcode
38	Can change verification code	10	change_verificationcode
39	Can delete verification code	10	delete_verificationcode
40	Can view verification code	10	view_verificationcode
41	Can add profile like	11	add_profilelike
42	Can change profile like	11	change_profilelike
43	Can delete profile like	11	delete_profilelike
44	Can view profile like	11	view_profilelike
45	Can add profile favorite	12	add_profilefavorite
46	Can change profile favorite	12	change_profilefavorite
47	Can delete profile favorite	12	delete_profilefavorite
48	Can view profile favorite	12	view_profilefavorite
49	Can add profile comment	13	add_profilecomment
50	Can change profile comment	13	change_profilecomment
51	Can delete profile comment	13	delete_profilecomment
52	Can view profile comment	13	view_profilecomment
53	Can add advertisement	14	add_advertisement
54	Can change advertisement	14	change_advertisement
55	Can delete advertisement	14	delete_advertisement
56	Can view advertisement	14	view_advertisement
57	Can add ban word	15	add_banword
58	Can change ban word	15	change_banword
59	Can delete ban word	15	delete_banword
60	Can view ban word	15	view_banword
61	Can add country	16	add_country
62	Can change country	16	change_country
63	Can delete country	16	delete_country
64	Can view country	16	view_country
65	Can add custom settings	17	add_customsettings
66	Can change custom settings	17	change_customsettings
67	Can delete custom settings	17	delete_customsettings
68	Can view custom settings	17	view_customsettings
69	Can add email fragment	18	add_emailfragment
70	Can change email fragment	18	change_emailfragment
71	Can delete email fragment	18	delete_emailfragment
72	Can view email fragment	18	view_emailfragment
73	Can add language	19	add_language
74	Can change language	19	change_language
75	Can delete language	19	delete_language
76	Can view language	19	view_language
77	Can add category film places	20	add_categoryfilmplaces
78	Can change category film places	20	change_categoryfilmplaces
79	Can delete category film places	20	delete_categoryfilmplaces
80	Can view category film places	20	view_categoryfilmplaces
81	Can add film places	21	add_filmplaces
82	Can change film places	21	change_filmplaces
83	Can delete film places	21	delete_filmplaces
84	Can view film places	21	view_filmplaces
85	Can add film request	22	add_filmrequest
86	Can change film request	22	change_filmrequest
87	Can delete film request	22	delete_filmrequest
88	Can view film request	22	view_filmrequest
89	Can add film places like	23	add_filmplaceslike
90	Can change film places like	23	change_filmplaceslike
91	Can delete film places like	23	delete_filmplaceslike
92	Can view film places like	23	view_filmplaceslike
93	Can add film places favorite	24	add_filmplacesfavorite
94	Can change film places favorite	24	change_filmplacesfavorite
95	Can delete film places favorite	24	delete_filmplacesfavorite
96	Can view film places favorite	24	view_filmplacesfavorite
97	Can add film places comment	25	add_filmplacescomment
98	Can change film places comment	25	change_filmplacescomment
99	Can delete film places comment	25	delete_filmplacescomment
100	Can view film places comment	25	view_filmplacescomment
101	Can add album	26	add_album
102	Can change album	26	change_album
103	Can delete album	26	delete_album
104	Can view album	26	view_album
105	Can add gallery	27	add_gallery
106	Can change gallery	27	change_gallery
107	Can delete gallery	27	delete_gallery
108	Can view gallery	27	view_gallery
109	Can add image	28	add_image
110	Can change image	28	change_image
111	Can delete image	28	delete_image
112	Can view image	28	view_image
113	Can add photo session	29	add_photosession
114	Can change photo session	29	change_photosession
115	Can delete photo session	29	delete_photosession
116	Can view photo session	29	view_photosession
117	Can add photo session like	30	add_photosessionlike
118	Can change photo session like	30	change_photosessionlike
119	Can delete photo session like	30	delete_photosessionlike
120	Can view photo session like	30	view_photosessionlike
121	Can add photo session favorite	31	add_photosessionfavorite
122	Can change photo session favorite	31	change_photosessionfavorite
123	Can delete photo session favorite	31	delete_photosessionfavorite
124	Can view photo session favorite	31	view_photosessionfavorite
125	Can add photo session comment	32	add_photosessioncomment
126	Can change photo session comment	32	change_photosessioncomment
127	Can delete photo session comment	32	delete_photosessioncomment
128	Can view photo session comment	32	view_photosessioncomment
129	Can add gallery like	33	add_gallerylike
130	Can change gallery like	33	change_gallerylike
131	Can delete gallery like	33	delete_gallerylike
132	Can view gallery like	33	view_gallerylike
133	Can add gallery favorite	34	add_galleryfavorite
134	Can change gallery favorite	34	change_galleryfavorite
135	Can delete gallery favorite	34	delete_galleryfavorite
136	Can view gallery favorite	34	view_galleryfavorite
137	Can add gallery comment	35	add_gallerycomment
138	Can change gallery comment	35	change_gallerycomment
139	Can delete gallery comment	35	delete_gallerycomment
140	Can view gallery comment	35	view_gallerycomment
141	Can add chat	36	add_chat
142	Can change chat	36	change_chat
143	Can delete chat	36	delete_chat
144	Can view chat	36	view_chat
145	Can add request chat	37	add_requestchat
146	Can change request chat	37	change_requestchat
147	Can delete request chat	37	delete_requestchat
148	Can view request chat	37	view_requestchat
149	Can add request message	38	add_requestmessage
150	Can change request message	38	change_requestmessage
151	Can delete request message	38	delete_requestmessage
152	Can view request message	38	view_requestmessage
153	Can add notification	39	add_notification
154	Can change notification	39	change_notification
155	Can delete notification	39	delete_notification
156	Can view notification	39	view_notification
157	Can add message	40	add_message
158	Can change message	40	change_message
159	Can delete message	40	delete_message
160	Can view message	40	view_message
161	Can add city	41	add_city
162	Can change city	41	change_city
163	Can delete city	41	delete_city
164	Can view city	41	view_city
165	Can add choice	42	add_choice
166	Can change choice	42	change_choice
167	Can delete choice	42	delete_choice
168	Can view choice	42	view_choice
169	Can add question	43	add_question
170	Can change question	43	change_question
171	Can delete question	43	delete_question
172	Can view question	43	view_question
173	Can add answer	44	add_answer
174	Can change answer	44	change_answer
175	Can delete answer	44	delete_answer
176	Can view answer	44	view_answer
177	Can add not auth film request	45	add_notauthfilmrequest
178	Can change not auth film request	45	change_notauthfilmrequest
179	Can delete not auth film request	45	delete_notauthfilmrequest
180	Can view not auth film request	45	view_notauthfilmrequest
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
15	pbkdf2_sha256$260000$a2vZYsFVi8WzPUrCkYvULa$ltz3OCf0vwJ1GH3Y6BJtEk9P+K9IwKuwyW6Wv8+WDp8=	2022-05-13 10:06:58.132055+00	f	masiasia@narod.ru				f	t	2022-05-13 09:44:20.330655+00
11	pbkdf2_sha256$260000$nQC6T6sAUQs1WJ0abJwxnz$VLeqBMynMLZO+Qh4Mxynh6idpOMa61oV+RsGXF/LTU4=	\N	f	EEEE@MAIL.COM				f	t	2022-04-16 15:28:13.579579+00
6	pbkdf2_sha256$260000$SWIngyN986zaVOIRjBaEco$/kj01/irNXRFPu2flKZtSrFpTHcGC820BEnIQnlghEg=	2022-04-18 13:50:23.027894+00	f	tsp7439@gmail.com				f	t	2022-04-07 09:47:20.122364+00
2	pbkdf2_sha256$260000$151q2teqosKY1HgyD7VhDS$10GI3+GIrDKerZyVSqSZcbZn9cD9SnZAv8jN9QdIGtw=	2022-04-07 11:39:05.329218+00	f	muzhyke1@gmail.com				f	t	2022-04-06 15:27:09.63288+00
12	pbkdf2_sha256$260000$4vtJCvcaXQmvTqJd883YNe$+Zl9WWzZYvdG10XQK63SWwa4SKvOi5sGRMGdCK6oJ6k=	\N	f	avramenkoa773@gmail.com				f	t	2022-04-28 18:22:34.612373+00
8	pbkdf2_sha256$260000$QiRCXD5xg8bz5IWH21185q$ZvHpyIN8eUGK8sKfoHJf8Zo+U8ZKF2uVivJYqTCmLuw=	2022-05-01 13:39:19.781899+00	f	joffreyprogamer@gmail.com				f	t	2022-04-07 14:06:56.937686+00
13	pbkdf2_sha256$260000$r9vy9AXbuC6oRQIkGcclnG$pv65pB3/ygO2Pkj87OCmbvoKYQO4WIm0J6UvCm5PWvI=	2022-05-10 10:22:26.026724+00	f	Slava_tuman@mail.ru				f	t	2022-05-10 10:21:20.12091+00
10	pbkdf2_sha256$260000$WKCwJd1UlbxB80kHTgDxwQ$arM+d7J51pjGpWW1CZSMqP5GVmc7JxlatzWhACfIt1o=	2022-05-10 11:50:00.89099+00	f	profotki@mail.ru				f	t	2022-04-08 17:34:37.320815+00
9	pbkdf2_sha256$260000$mtqba6pjzCCjOUHe3zqHI1$C3+1y+6IiHC1NqrTIbpFo1qwsL4Q9XMxN8nLBnN/NXI=	2022-04-11 19:43:11.84456+00	f	muzhyke@gmail.com				f	t	2022-04-08 16:59:26.526535+00
7	pbkdf2_sha256$260000$dJRTcsGr5Ixkg3AIkAq7Gv$B43lqaJNLcyiz1SiUgo3Em2eBpLFwJnINYfLBz2xwtE=	2022-05-10 11:59:55.568116+00	f	joffreywebd@gmail.com				f	t	2022-04-07 11:41:59.784656+00
1	pbkdf2_sha256$260000$kq8UlHIPtENFdvwzzdS1TR$rvmfj7rGC68eVrW5A/UMoP9J8mHV/NQW5mKcA/yhxmo=	2022-05-13 09:18:27.196472+00	t	admin				t	t	2022-04-05 10:08:31.120763+00
14	pbkdf2_sha256$260000$vvAY9wCopssikvPQNYZsb7$8FfVOnTIkh4SXdEtng+kjNYeYWGiwQOn/ZBKTQ4SJO4=	2022-05-13 09:19:34.008448+00	f	leksich3@gmail.com				f	t	2022-05-13 09:18:53.704157+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: chat_chat; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.chat_chat (id, receiver_id_id, sender_id_id, is_receiver_hide_chat, is_sender_hide_chat) FROM stdin;
1	6	7	f	f
2	7	7	f	f
4	10	10	f	f
5	9	10	f	f
6	8	10	f	f
7	7	8	f	f
8	7	10	f	f
9	9	7	f	f
10	15	10	f	f
\.


--
-- Data for Name: chat_message; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.chat_message (id, content, "timestamp", status_read, author_id, chat_id) FROM stdin;
1	a	2022-04-07 22:36:50.83584+00	f	7	1
2	s	2022-04-07 22:36:50.894397+00	f	7	1
3	d	2022-04-07 22:36:50.95068+00	f	7	1
4	f	2022-04-07 22:36:51.088465+00	f	7	1
5	a	2022-04-07 22:36:51.134744+00	f	7	1
6	s	2022-04-07 22:36:51.18768+00	f	7	1
7	d	2022-04-07 22:36:51.269491+00	f	7	1
8	f	2022-04-07 22:36:51.54079+00	f	7	1
9	s	2022-04-07 22:36:51.594422+00	f	7	1
10	a	2022-04-07 22:36:51.648073+00	f	7	1
11	d	2022-04-07 22:36:51.699383+00	f	7	1
12	f	2022-04-07 22:36:51.81811+00	f	7	1
13	a	2022-04-07 22:36:51.862284+00	f	7	1
14	s	2022-04-07 22:36:51.905541+00	f	7	1
15	d	2022-04-07 22:36:52.023674+00	f	7	1
16	f	2022-04-07 22:36:52.128884+00	f	7	1
17	a	2022-04-07 22:36:52.265261+00	f	7	1
18	s	2022-04-07 22:36:52.318411+00	f	7	1
19	d	2022-04-07 22:36:52.368675+00	f	7	1
20	f	2022-04-07 22:36:52.477361+00	f	7	1
21	a	2022-04-07 22:36:52.590108+00	f	7	1
22	s	2022-04-07 22:36:52.650724+00	f	7	1
23	d	2022-04-07 22:36:52.705963+00	f	7	1
24	f	2022-04-07 22:36:52.844681+00	f	7	1
25	a	2022-04-07 22:36:52.955786+00	f	7	1
26	s	2022-04-07 22:36:53.00173+00	f	7	1
27	d	2022-04-07 22:36:53.118412+00	f	7	1
28	f	2022-04-07 22:36:53.229373+00	f	7	1
29	a	2022-04-07 22:36:53.320103+00	f	7	1
30	s	2022-04-07 22:36:53.377261+00	f	7	1
31	d	2022-04-07 22:36:53.459655+00	f	7	1
32	f	2022-04-07 22:36:53.566644+00	f	7	1
33	a	2022-04-07 22:36:53.63775+00	f	7	1
34	s	2022-04-07 22:36:53.698041+00	f	7	1
35	d	2022-04-07 22:36:53.754116+00	f	7	1
36	f	2022-04-07 22:36:53.884811+00	f	7	1
37	a	2022-04-07 22:36:53.943269+00	f	7	1
38	s	2022-04-07 22:36:53.989686+00	f	7	1
39	d	2022-04-07 22:36:54.070959+00	f	7	1
40	f	2022-04-07 22:36:54.194926+00	f	7	1
41	a	2022-04-07 22:36:54.255374+00	f	7	1
42	s	2022-04-07 22:36:54.312325+00	f	7	1
43	d	2022-04-07 22:36:54.380052+00	f	7	1
44	f	2022-04-07 22:36:54.556845+00	f	7	1
45	a	2022-04-07 22:36:54.613935+00	f	7	1
46	s	2022-04-07 22:36:54.680577+00	f	7	1
47	d	2022-04-07 22:36:54.72783+00	f	7	1
48	f	2022-04-07 22:36:54.809534+00	f	7	1
49	a	2022-04-07 22:36:54.868909+00	f	7	1
50	s	2022-04-07 22:36:54.932667+00	f	7	1
51	d	2022-04-07 22:36:54.993955+00	f	7	1
52	f	2022-04-07 22:36:55.132067+00	f	7	1
53	a	2022-04-07 22:36:55.235704+00	f	7	1
54	s	2022-04-07 22:36:55.278879+00	f	7	1
55	d	2022-04-07 22:36:55.324703+00	f	7	1
56	f	2022-04-07 22:36:55.435457+00	f	7	1
57	a	2022-04-07 22:36:55.499585+00	f	7	1
58	s	2022-04-07 22:36:55.557677+00	f	7	1
59	d	2022-04-07 22:36:55.615719+00	f	7	1
60	f	2022-04-07 22:36:55.747149+00	f	7	1
61	a	2022-04-07 22:36:55.789507+00	f	7	1
62	s	2022-04-07 22:36:55.833183+00	f	7	1
63	d	2022-04-07 22:36:55.913857+00	f	7	1
64	f	2022-04-07 22:37:49.056754+00	f	7	1
65	g	2022-04-07 22:37:49.174143+00	f	7	1
66	s	2022-04-07 22:37:49.240912+00	f	7	1
67	d	2022-04-07 22:37:49.283926+00	f	7	1
68	f	2022-04-07 22:37:49.419657+00	f	7	1
69	g	2022-04-07 22:37:49.527265+00	f	7	1
70	s	2022-04-07 22:37:49.632262+00	f	7	1
71	d	2022-04-07 22:37:49.687064+00	f	7	1
72	f	2022-04-07 22:37:49.796021+00	f	7	1
73	g	2022-04-07 22:37:49.89256+00	f	7	1
74	s	2022-04-07 22:37:49.995757+00	f	7	1
75	d	2022-04-07 22:37:50.036448+00	f	7	1
76	f	2022-04-07 22:37:50.143194+00	f	7	1
77	g	2022-04-07 22:37:50.265991+00	f	7	1
78	s	2022-04-07 22:37:50.310711+00	f	7	1
79	d	2022-04-07 22:37:50.360336+00	f	7	1
80	f	2022-04-07 22:37:50.463484+00	f	7	1
81	g	2022-04-07 22:37:50.590233+00	f	7	1
82	s	2022-04-07 22:37:50.632447+00	f	7	1
83	d	2022-04-07 22:37:50.735493+00	f	7	1
84	f	2022-04-07 22:37:50.794305+00	f	7	1
85	g	2022-04-07 22:37:50.907401+00	f	7	1
86	s	2022-04-07 22:37:50.987696+00	f	7	1
87	d	2022-04-07 22:37:51.074027+00	f	7	1
88	f	2022-04-07 22:37:51.127878+00	f	7	1
89	g	2022-04-07 22:37:51.234357+00	f	7	1
90	s	2022-04-07 22:37:51.37704+00	f	7	1
91	d	2022-04-07 22:37:51.430543+00	f	7	1
92	f	2022-04-07 22:37:51.486457+00	f	7	1
93	123	2022-04-07 23:02:29.231804+00	f	7	1
94	Привет	2022-04-07 23:08:00.420444+00	f	7	2
95	123	2022-04-08 13:22:29.010676+00	f	7	1
96	123	2022-04-08 13:30:35.793509+00	f	7	1
97	1	2022-04-08 13:37:14.171903+00	f	6	1
98	й23	2022-04-08 13:43:26.394247+00	f	6	1
99	123	2022-04-08 13:45:37.248283+00	f	7	1
100	gf	2022-04-08 15:01:18.007738+00	f	7	1
101	123	2022-04-08 15:02:44.598843+00	f	7	1
102	hello	2022-04-08 15:02:52.171391+00	f	7	1
103	how are u	2022-04-08 15:02:55.264334+00	f	7	1
104	Привет. Тестовое сообщение)	2022-04-09 12:44:35.367146+00	f	10	5
105	окей	2022-04-11 19:46:00.955536+00	f	9	5
106	123	2022-04-13 12:50:57.20423+00	f	7	1
107	привет	2022-04-13 18:33:41.851229+00	f	8	7
108	123	2022-04-13 18:34:04.052107+00	f	8	7
109	123	2022-04-13 19:01:46.36677+00	f	8	7
110	Кстати, треугольничек отправки не работает :) Забыл сказать. А в запросах по моему работает.	2022-04-15 09:39:31.630541+00	f	10	5
111	Тест с телефона.	2022-05-10 11:51:21.345459+00	f	10	5
112	123	2022-05-10 11:54:17.979193+00	f	7	9
113	123	2022-05-11 07:30:22.641964+00	f	7	8
114	Тест	2022-05-11 10:13:39.485287+00	f	10	6
\.


--
-- Data for Name: chat_notification; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.chat_notification (id, type_note, text_note, is_read, "timestamp", model_id, receiver_id, sender_id) FROM stdin;
\.


--
-- Data for Name: chat_requestchat; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.chat_requestchat (id, request_receiver_id, request_sender_id) FROM stdin;
3	8	7
4	7	8
5	9	8
6	9	8
7	9	10
8	9	6
9	10	10
10	8	7
11	7	8
12	8	7
13	8	7
14	8	7
15	8	7
16	7	8
17	8	7
18	7	10
19	15	10
\.


--
-- Data for Name: chat_requestmessage; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.chat_requestmessage (id, content, "timestamp", status_read, author_id, chat_id, request_id) FROM stdin;
1		2022-04-13 14:49:48.117051+00	f	7	3	4
2		2022-04-13 16:01:10.734073+00	f	8	4	5
3		2022-04-13 16:02:39.164176+00	f	8	5	6
4		2022-04-13 16:03:29.672525+00	f	8	6	7
5	привет	2022-04-13 18:31:50.447208+00	f	8	6	\N
6	123	2022-04-13 18:33:08.350681+00	f	8	6	\N
7	как едал	2022-04-13 18:33:11.89313+00	f	8	6	\N
8	123	2022-04-13 19:02:33.315213+00	f	8	6	\N
9	123	2022-04-13 19:09:32.134705+00	f	7	4	\N
10		2022-04-14 09:46:20.676481+00	f	10	7	8
11	Прошло очень много лет, а вы не ответили, готовы ли вы взять заказ? :)	2022-04-14 10:14:29.953056+00	f	10	7	\N
12	Да, тут треугольничек отправки сообщения работает.	2022-04-15 09:39:56.344196+00	f	10	7	\N
13		2022-04-18 13:51:43.370007+00	f	6	8	9
14	че как	2022-04-18 13:52:01.721316+00	f	6	8	\N
15	раз	2022-04-18 13:52:32.774185+00	f	6	8	\N
16	два три	2022-04-18 13:52:34.041937+00	f	6	8	\N
17	пппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппппп	2022-04-18 13:52:46.314371+00	f	6	8	\N
18		2022-04-20 04:04:45.264716+00	f	10	9	10
19		2022-04-22 23:03:07.902943+00	f	7	10	11
20		2022-04-22 23:45:42.068506+00	f	8	11	12
21	123	2022-04-28 17:26:15.395013+00	f	7	11	\N
22	123	2022-04-28 17:26:26.199494+00	f	7	11	\N
23	3	2022-04-28 17:26:46.622549+00	f	7	11	\N
24		2022-05-01 13:33:42.811391+00	f	7	12	13
25		2022-05-01 13:57:27.217435+00	f	7	13	14
26		2022-05-01 14:04:54.687677+00	f	7	14	15
27		2022-05-01 14:06:31.308481+00	f	7	15	16
28		2022-05-01 14:56:31.434312+00	f	8	16	17
29		2022-05-01 14:57:43.45042+00	f	7	17	18
30		2022-05-11 15:59:25.300952+00	f	10	18	19
31	123	2022-05-12 10:04:06.164057+00	f	10	9	\N
32		2022-05-13 10:01:49.125132+00	f	10	19	20
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-04-05 11:15:01.687341+00	1	admin	2	[{"changed": {"fields": ["Name", "Surname", "String location", "Phone", "Email", "String location now", "Last views"]}}]	8	1
2	2022-04-05 11:15:09.396448+00	1	admin	2	[{"changed": {"fields": ["Views"]}}]	8	1
3	2022-04-05 11:15:39.669609+00	1	Фотографы	1	[{"added": {}}]	7	1
4	2022-04-05 11:15:44.696909+00	2	Визажисты	1	[{"added": {}}]	7	1
5	2022-04-05 11:15:49.858577+00	3	Модели	1	[{"added": {}}]	7	1
6	2022-04-05 11:15:54.019817+00	4	Фотостудии	1	[{"added": {}}]	7	1
7	2022-04-05 11:15:59.569339+00	5	Фотопечать	1	[{"added": {}}]	7	1
8	2022-04-05 11:16:03.036598+00	6	Аренда	1	[{"added": {}}]	7	1
9	2022-04-05 11:16:10.073935+00	7	Видеографы	1	[{"added": {}}]	7	1
10	2022-04-05 11:16:16.744393+00	8	Фотошколы	1	[{"added": {}}]	7	1
11	2022-04-05 11:16:19.515451+00	9	Ретушеры	1	[{"added": {}}]	7	1
12	2022-04-05 11:16:27.451481+00	10	Декораторы	1	[{"added": {}}]	7	1
13	2022-04-05 11:16:31.257303+00	11	Организатор	1	[{"added": {}}]	7	1
14	2022-04-05 11:18:20.990323+00	1	Животные	1	[{"added": {}}]	9	1
15	2022-04-05 11:18:23.897382+00	2	Архитектура	1	[{"added": {}}]	9	1
16	2022-04-05 11:18:29.906725+00	3	Репортаж	1	[{"added": {}}]	9	1
17	2022-04-05 11:18:33.346458+00	4	Дети	1	[{"added": {}}]	9	1
18	2022-04-05 11:18:38.069413+00	5	Семья	1	[{"added": {}}]	9	1
19	2022-04-05 11:18:41.746467+00	6	Беременные	1	[{"added": {}}]	9	1
20	2022-04-05 11:18:47.431187+00	7	Аэросъемки	1	[{"added": {}}]	9	1
21	2022-04-05 11:18:49.789683+00	8	Видеосъемка	1	[{"added": {}}]	9	1
22	2022-04-05 11:18:51.219508+00	8	Видеосъемка	2	[]	9	1
23	2022-04-05 11:18:56.175993+00	9	Интерьеры	1	[{"added": {}}]	9	1
24	2022-04-05 11:18:59.7885+00	10	Новорожденные	1	[{"added": {}}]	9	1
25	2022-04-05 11:19:08.800311+00	11	Обучение фотографии	1	[{"added": {}}]	9	1
26	2022-04-05 11:19:11.158561+00	12	Портрет	1	[{"added": {}}]	9	1
27	2022-04-05 11:19:16.676957+00	13	Предметная съемка	1	[{"added": {}}]	9	1
28	2022-04-05 11:19:19.176109+00	14	Каталожная съемка	1	[{"added": {}}]	9	1
29	2022-04-05 11:19:24.87357+00	15	Реклама	1	[{"added": {}}]	9	1
30	2022-04-05 11:19:27.614194+00	16	Свадебные	1	[{"added": {}}]	9	1
31	2022-04-05 11:19:33.443511+00	17	Food	1	[{"added": {}}]	9	1
32	2022-04-05 11:19:37.323575+00	18	Love Story	1	[{"added": {}}]	9	1
33	2022-04-05 11:19:42.080616+00	19	Ню	1	[{"added": {}}]	9	1
34	2022-04-05 11:19:45.934148+00	20	3d фотографы	1	[{"added": {}}]	9	1
35	2022-04-05 11:21:11.104968+00	1	1	1	[{"added": {}}]	28	1
36	2022-04-05 11:21:30.435296+00	1	Разное	2	[{"changed": {"fields": ["Main photo id"]}}]	26	1
37	2022-04-05 11:22:03.990782+00	1	Language object (1)	1	[{"added": {}}]	19	1
38	2022-04-05 11:22:08.731131+00	2	Language object (2)	1	[{"added": {}}]	19	1
39	2022-04-05 11:22:15.615441+00	3	Language object (3)	1	[{"added": {}}]	19	1
40	2022-04-05 11:22:22.015221+00	4	Language object (4)	1	[{"added": {}}]	19	1
41	2022-04-05 11:22:25.261186+00	5	Language object (5)	1	[{"added": {}}]	19	1
42	2022-04-05 11:22:31.076874+00	6	Language object (6)	1	[{"added": {}}]	19	1
43	2022-04-05 11:22:44.854724+00	1	EmailFragment object (1)	1	[{"added": {}}]	18	1
44	2022-04-05 11:22:56.241555+00	1	CustomSettings object (1)	1	[{"added": {}}]	17	1
45	2022-04-06 13:04:18.518267+00	72	Бахчисарай Оспаривается	2	[{"changed": {"fields": ["City name"]}}]	41	1
46	2022-04-06 13:04:23.522262+00	75	Белая Холуница	2	[{"changed": {"fields": ["City name"]}}]	41	1
47	2022-04-06 13:04:28.802128+00	74	Белая Калитва	2	[{"changed": {"fields": ["City name"]}}]	41	1
48	2022-04-06 13:05:07.673872+00	1052	Щёлкино Оспаривается	2	[{"changed": {"fields": ["City name"]}}]	41	1
49	2022-04-06 13:07:25.381643+00	888	Старый Крым Оспаривается	2	[{"changed": {"fields": ["City name"]}}]	41	1
50	2022-04-06 13:08:16.556534+00	72	Бахчисарай	2	[{"changed": {"fields": ["City name"]}}]	41	1
51	2022-04-06 13:08:37.598951+00	150	Верхняя Тура	2	[{"changed": {"fields": ["City name"]}}]	41	1
52	2022-04-06 13:08:42.173954+00	140	Великий Устюг	2	[{"changed": {"fields": ["City name"]}}]	41	1
53	2022-04-06 13:09:15.144197+00	117	Большой Камень	2	[{"changed": {"fields": ["City name"]}}]	41	1
54	2022-04-06 13:09:26.304188+00	139	Великий Новгород	2	[{"changed": {"fields": ["City name"]}}]	41	1
55	2022-04-06 13:09:31.115029+00	138	Великие Луки	2	[{"changed": {"fields": ["City name"]}}]	41	1
56	2022-04-06 13:09:40.241293+00	146	Верхний Тагил	2	[{"changed": {"fields": ["City name"]}}]	41	1
57	2022-04-06 13:09:46.35902+00	149	Верхняя Салда	2	[{"changed": {"fields": ["City name"]}}]	41	1
58	2022-04-06 13:09:52.181577+00	148	Верхняя Пышма	2	[{"changed": {"fields": ["City name"]}}]	41	1
59	2022-04-06 13:10:00.021114+00	147	Верхний Уфалей	2	[{"changed": {"fields": ["City name"]}}]	41	1
60	2022-04-06 13:11:46.75749+00	192	Гаврилов Посад	2	[{"changed": {"fields": ["City name"]}}]	41	1
61	2022-04-06 13:11:51.047112+00	191	Вятские Поляны	2	[{"changed": {"fields": ["City name"]}}]	41	1
62	2022-04-06 13:11:56.629465+00	187	Вышний Волочёк	2	[{"changed": {"fields": ["City name"]}}]	41	1
63	2022-04-06 13:12:07.068575+00	211	Горячий Ключ	2	[{"changed": {"fields": ["City name"]}}]	41	1
64	2022-04-06 13:12:16.305291+00	229	Дагестанские Огни	2	[{"changed": {"fields": ["City name"]}}]	41	1
65	2022-04-06 13:12:54.815683+00	382	КерчьОспаривается	3		41	1
66	2022-04-06 13:13:20.7088+00	294	Западная Двина	2	[{"changed": {"fields": ["City name"]}}]	41	1
67	2022-04-06 13:13:39.191975+00	465	Красный Холм	2	[{"changed": {"fields": ["City name"]}}]	41	1
68	2022-04-06 13:13:45.512659+00	464	Красный Сулин	2	[{"changed": {"fields": ["City name"]}}]	41	1
69	2022-04-06 13:13:49.716258+00	463	Красный Кут	2	[{"changed": {"fields": ["City name"]}}]	41	1
70	2022-04-06 13:14:28.625808+00	570	Минеральные Воды	2	[{"changed": {"fields": ["City name"]}}]	41	1
71	2022-04-06 13:14:34.877725+00	551	Мариинский Посад	2	[{"changed": {"fields": ["City name"]}}]	41	1
72	2022-04-06 13:14:42.553797+00	542	Малая Вишера	2	[{"changed": {"fields": ["City name"]}}]	41	1
73	2022-04-06 13:14:54.695234+00	519	Лодейное Поле	2	[{"changed": {"fields": ["City name"]}}]	41	1
74	2022-04-06 13:15:25.009434+00	630	Нижний Новгород	2	[{"changed": {"fields": ["City name"]}}]	41	1
75	2022-04-06 13:15:33.155893+00	667	Новый Уренгой	2	[{"changed": {"fields": ["City name"]}}]	41	1
76	2022-04-06 13:15:36.80859+00	666	Новый Оскол	2	[{"changed": {"fields": ["City name"]}}]	41	1
77	2022-04-06 13:16:02.465962+00	633	Нижняя Тура	2	[{"changed": {"fields": ["City name"]}}]	41	1
78	2022-04-06 13:16:10.168856+00	632	Нижняя Салда	2	[{"changed": {"fields": ["City name"]}}]	41	1
79	2022-04-06 13:16:14.722747+00	631	Нижний Тагил	2	[{"changed": {"fields": ["City name"]}}]	41	1
80	2022-04-06 13:16:20.759977+00	629	Нижний Ломов	2	[{"changed": {"fields": ["City name"]}}]	41	1
81	2022-04-06 13:16:27.401059+00	628	Нижние Серги	2	[{"changed": {"fields": ["City name"]}}]	41	1
82	2022-04-06 13:16:37.641155+00	597	Набережные Челны	2	[{"changed": {"fields": ["City name"]}}]	41	1
83	2022-04-06 13:16:53.722532+00	747	Полярные Зори	2	[{"changed": {"fields": ["City name"]}}]	41	1
84	2022-04-06 13:17:05.337401+00	713	Павловский Посад	2	[{"changed": {"fields": ["City name"]}}]	41	1
85	2022-04-06 13:17:22.117815+00	872	Сосновый Бор	2	[{"changed": {"fields": ["City name"]}}]	41	1
86	2022-04-06 13:17:31.636758+00	858	Советская Гавань	2	[{"changed": {"fields": ["City name"]}}]	41	1
87	2022-04-06 13:17:38.327285+00	837	Сергиев Посад	2	[{"changed": {"fields": ["City name"]}}]	41	1
88	2022-04-06 13:18:08.467187+00	888	Старый Крым Оспаривается	3		41	1
89	2022-04-06 13:18:15.690501+00	884	Старая Купавна	2	[{"changed": {"fields": ["City name"]}}]	41	1
90	2022-04-06 13:18:20.321497+00	885	Старая Русса	2	[{"changed": {"fields": ["City name"]}}]	41	1
91	2022-04-06 13:18:25.688785+00	889	Старый Оскол	2	[{"changed": {"fields": ["City name"]}}]	41	1
92	2022-04-06 15:52:10.103562+00	1	admin	2	[{"changed": {"fields": ["Phone", "Email"]}}]	8	1
93	2022-04-06 16:00:31.519712+00	3	tsp7439@gmail.com	3		4	1
94	2022-04-06 16:03:08.961447+00	4	tsp7439@gmail.com	3		4	1
95	2022-04-06 16:10:19.347867+00	5	tsp7439@gmail.com	3		4	1
96	2022-04-06 16:56:33.13018+00	1	admin	2	[{"changed": {"fields": ["Phone", "Email"]}}]	8	1
97	2022-04-07 09:47:12.633356+00	1	admin	2	[{"changed": {"fields": ["Phone", "Email"]}}]	8	1
98	2022-04-07 09:52:56.297207+00	3	3	3		28	1
99	2022-04-07 09:52:56.301168+00	2	2	3		28	1
100	2022-04-08 09:35:43.291194+00	1	Архитектура	1	[{"added": {}}]	20	1
101	2022-04-08 09:35:49.076267+00	2	Горы	1	[{"added": {}}]	20	1
102	2022-04-08 09:35:55.264992+00	3	Город	1	[{"added": {}}]	20	1
103	2022-04-08 09:35:58.205358+00	4	Интерьер	1	[{"added": {}}]	20	1
104	2022-04-08 09:36:04.857277+00	5	Лес	1	[{"added": {}}]	20	1
105	2022-04-08 09:36:09.800535+00	6	Море	1	[{"added": {}}]	20	1
106	2022-04-08 09:36:12.523894+00	7	Природа	1	[{"added": {}}]	20	1
107	2022-04-08 09:36:19.089256+00	8	Парк	1	[{"added": {}}]	20	1
108	2022-04-08 09:36:21.569842+00	9	Улицы	1	[{"added": {}}]	20	1
109	2022-04-08 09:36:28.04776+00	10	Фотостудия	1	[{"added": {}}]	20	1
110	2022-04-08 09:36:30.671581+00	11	Церковь	1	[{"added": {}}]	20	1
111	2022-04-08 09:36:33.412223+00	12	Пейзаж	1	[{"added": {}}]	20	1
112	2022-04-08 09:36:41.51375+00	13	Детский мир	1	[{"added": {}}]	20	1
113	2022-04-08 09:36:44.258039+00	14	Путешествия	1	[{"added": {}}]	20	1
114	2022-04-08 09:36:51.155796+00	15	Спорт	1	[{"added": {}}]	20	1
115	2022-04-08 09:36:54.468439+00	16	Общепит	1	[{"added": {}}]	20	1
116	2022-04-08 09:36:57.07893+00	17	Без категории	1	[{"added": {}}]	20	1
117	2022-04-08 10:05:54.597416+00	3	3	1	[{"added": {}}]	36	1
118	2022-04-08 10:35:48.172832+00	1	admin	2	[{"changed": {"fields": ["Email", "Email verify"]}}]	8	1
119	2022-04-12 08:28:22.754091+00	3	3	3		36	1
120	2022-04-13 13:13:55.237711+00	2	FilmRequest object (2)	3		22	1
121	2022-04-13 13:13:55.245186+00	1	FilmRequest object (1)	3		22	1
122	2022-04-19 08:53:58.642778+00	10	profotki@mail.ru	2	[{"changed": {"fields": ["Date stay start", "Date stay end", "Message"]}}]	8	1
123	2022-05-01 14:49:09.11359+00	15	FilmRequest object (15)	2	[{"changed": {"fields": ["Filming status"]}}]	22	1
124	2022-05-13 11:38:17.490863+00	1	Advertisement object (1)	1	[{"added": {}}]	14	1
125	2022-05-13 11:40:58.238042+00	1	Advertisement object (1)	2	[]	14	1
126	2022-05-13 11:43:51.301529+00	1	Advertisement object (1)	2	[]	14	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	accounts	procategory
8	accounts	profile
9	accounts	specialization
10	accounts	verificationcode
11	accounts	profilelike
12	accounts	profilefavorite
13	accounts	profilecomment
14	additional_entities	advertisement
15	additional_entities	banword
16	additional_entities	country
17	additional_entities	customsettings
18	additional_entities	emailfragment
19	additional_entities	language
20	film_places	categoryfilmplaces
21	film_places	filmplaces
22	film_places	filmrequest
23	film_places	filmplaceslike
24	film_places	filmplacesfavorite
25	film_places	filmplacescomment
26	gallery	album
27	gallery	gallery
28	gallery	image
29	gallery	photosession
30	gallery	photosessionlike
31	gallery	photosessionfavorite
32	gallery	photosessioncomment
33	gallery	gallerylike
34	gallery	galleryfavorite
35	gallery	gallerycomment
36	chat	chat
37	chat	requestchat
38	chat	requestmessage
39	chat	notification
40	chat	message
41	additional_entities	city
42	additional_entities	choice
43	additional_entities	question
44	additional_entities	answer
45	film_places	notauthfilmrequest
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-04-04 17:58:28.852766+00
2	auth	0001_initial	2022-04-04 17:58:29.004344+00
3	additional_entities	0001_initial	2022-04-04 17:58:29.067231+00
4	accounts	0001_initial	2022-04-04 17:58:29.379831+00
5	admin	0001_initial	2022-04-04 17:58:29.435238+00
6	admin	0002_logentry_remove_auto_add	2022-04-04 17:58:29.455742+00
7	admin	0003_logentry_add_action_flag_choices	2022-04-04 17:58:29.475678+00
8	contenttypes	0002_remove_content_type_name	2022-04-04 17:58:29.541101+00
9	auth	0002_alter_permission_name_max_length	2022-04-04 17:58:29.565104+00
10	auth	0003_alter_user_email_max_length	2022-04-04 17:58:29.581671+00
11	auth	0004_alter_user_username_opts	2022-04-04 17:58:29.594575+00
12	auth	0005_alter_user_last_login_null	2022-04-04 17:58:29.608537+00
13	auth	0006_require_contenttypes_0002	2022-04-04 17:58:29.611706+00
14	auth	0007_alter_validators_add_error_messages	2022-04-04 17:58:29.628709+00
15	auth	0008_alter_user_username_max_length	2022-04-04 17:58:29.65039+00
16	auth	0009_alter_user_last_name_max_length	2022-04-04 17:58:29.733211+00
17	auth	0010_alter_group_name_max_length	2022-04-04 17:58:29.752261+00
18	auth	0011_update_proxy_permissions	2022-04-04 17:58:29.772665+00
19	auth	0012_alter_user_first_name_max_length	2022-04-04 17:58:29.785808+00
20	gallery	0001_initial	2022-04-04 17:58:30.342669+00
21	film_places	0001_initial	2022-04-04 17:58:30.778344+00
22	chat	0001_initial	2022-04-04 17:58:31.097303+00
23	sessions	0001_initial	2022-04-04 17:58:31.122353+00
24	additional_entities	0002_city	2022-04-06 12:59:14.802874+00
25	accounts	0002_profile_is_change	2022-04-07 12:42:14.173401+00
26	film_places	0002_auto_20220408_1334	2022-04-08 10:34:27.78055+00
27	additional_entities	0003_answer_choice_question	2022-04-08 15:24:15.620766+00
28	accounts	0003_alter_profile_string_location_now	2022-04-09 17:06:21.691246+00
29	additional_entities	0004_auto_20220409_2006	2022-04-09 17:06:21.846452+00
30	gallery	0002_auto_20220409_2006	2022-04-09 17:06:22.078689+00
31	accounts	0004_alter_profile_type_pro	2022-04-12 08:37:27.545456+00
32	chat	0002_auto_20220412_1854	2022-04-12 15:54:26.94576+00
33	film_places	0003_auto_20220413_1539	2022-04-13 12:39:28.629809+00
34	film_places	0004_filmrequest_reason_failure	2022-04-13 16:49:09.699326+00
35	additional_entities	0005_emailfragment_verify_email_for_not_auth_request	2022-04-14 14:59:42.839445+00
36	film_places	0005_auto_20220414_1759	2022-04-14 14:59:43.030133+00
37	accounts	0005_auto_20220419_1538	2022-04-19 12:38:37.796564+00
38	additional_entities	0006_customsettings_days_request_to_not_auth_user	2022-04-19 12:38:37.810962+00
39	accounts	0006_alter_profile_ready_status	2022-04-20 11:31:37.822869+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
k24a0ygal0g70udwrdou8vzkc49bfmmb	.eJxVjEEOwiAQRe_C2hChdGBcuu8ZyDCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-juIilDj9boH4keoO4p3qrUludV3mIHdFHrTLqcX0vB7u30GhXr41GhgzAmkig5hdGEbOjiOHgZ0ZrHN4BszBGtLKBKshalQE4JJKOoJ4fwDfbTeW:1nh8RY:7GXdPWybEcGhArfVl538HBRYnT3fEyxQjD1KAglclcY	2022-05-04 11:24:20.758468+00
jggmvi0dqlcxi70cduqoomum38urgnjg	.eJxVjEEOwiAQRe_C2hChdGBcuu8ZyDCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-juIilDj9boH4keoO4p3qrUludV3mIHdFHrTLqcX0vB7u30GhXr41GhgzAmkig5hdGEbOjiOHgZ0ZrHN4BszBGtLKBKshalQE4JJKOoJ4fwDfbTeW:1nl8pu:oPGcZey_dVU0lH3dwfAXdiXv_6Avx1Hzg9jlCFUxq74	2022-05-15 12:38:02.680081+00
68ygnclp0ufh6w67vfth2vnxbb8rk4zg	.eJxVjEEOwiAQRe_C2hChdGBcuu8ZyDCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-juIilDj9boH4keoO4p3qrUludV3mIHdFHrTLqcX0vB7u30GhXr41GhgzAmkig5hdGEbOjiOHgZ0ZrHN4BszBGtLKBKshalQE4JJKOoJ4fwDfbTeW:1nlDTw:apfpq8Oen2xFwyTTk_mIl3UKeV3Q8tD0EwWWr74jj4s	2022-05-15 17:35:40.670796+00
gmf3g87g9zq87n6ew7myuzkk1jc5l446	.eJxVjEEOwiAQRe_C2hChdGBcuu8ZyDCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-juIilDj9boH4keoO4p3qrUludV3mIHdFHrTLqcX0vB7u30GhXr41GhgzAmkig5hdGEbOjiOHgZ0ZrHN4BszBGtLKBKshalQE4JJKOoJ4fwDfbTeW:1npRRL:38mbaBkzXto-fzbp2F568-kgFDk21aGx1QGTSMMQWG8	2022-05-27 09:18:27.264667+00
\.


--
-- Data for Name: film_places_categoryfilmplaces; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_categoryfilmplaces (id, name_category) FROM stdin;
1	Архитектура
2	Горы
3	Город
4	Интерьер
5	Лес
6	Море
7	Природа
8	Парк
9	Улицы
10	Фотостудия
11	Церковь
12	Пейзаж
13	Детский мир
14	Путешествия
15	Спорт
16	Общепит
17	Без категории
\.


--
-- Data for Name: film_places_filmplaces; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplaces (id, name_place, description, photo_camera, cost, payment, place_location, string_place_location, views, last_views, last_ip_user, is_hidden, was_added, main_photo_id, profile_id) FROM stdin;
3	Место		тест	5000	TFP	0101000020E6100000E44BE8C101E14B400809512ED1F24240	Россия, Московская область	11	11	91.245.140.119	f	2022-04-16 08:25:21.153152+00	31	7
8	Город	Чудесные фото города.	Canon	5000	По предоплате	0101000020E61000005D0D759806024D400A09511A571D4C40	Россия, Пермь	1	1	91.245.140.119	f	2022-05-12 16:09:04.658603+00	49	10
1	Место 1	Описание	Фотик	5000	По предоплате	0101000020E6100000AE09832EC3E54B400709512E6DB14240	Россия, Москва	13	13	31.148.21.89	f	2022-04-08 11:44:11.051495+00	10	7
\.


--
-- Data for Name: film_places_filmplaces_category; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplaces_category (id, filmplaces_id, categoryfilmplaces_id) FROM stdin;
1	1	4
3	3	5
8	8	1
\.


--
-- Data for Name: film_places_filmplaces_place_image; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplaces_place_image (id, filmplaces_id, image_id) FROM stdin;
1	1	8
2	1	9
3	1	10
4	1	7
7	3	32
8	3	31
15	8	49
16	8	50
17	8	51
18	8	52
\.


--
-- Data for Name: film_places_filmplacescomment; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplacescomment (id, content, "timestamp", answer_id_comment_id, place_id, quote_id_id, sender_comment_id) FROM stdin;
\.


--
-- Data for Name: film_places_filmplacesfavorite; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplacesfavorite (id, place_id, profile_id) FROM stdin;
1	1	7
2	1	10
\.


--
-- Data for Name: film_places_filmplaceslike; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmplaceslike (id, place_id, profile_id) FROM stdin;
\.


--
-- Data for Name: film_places_filmrequest; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_filmrequest (id, filming_timestamp, hours_duration, filming_type, filming_status, count_person, filming_budget, need_makeup_artist, description, was_added, profile_id, place_filming, receiver_profile_id, reason_failure) FROM stdin;
3	2022-04-03 14:34:00+00	5	свадебная	NEW	5	5000	f	лалала	2022-04-13 14:35:43.145994+00	7	\N	8	\N
4	2022-04-03 14:34:00+00	5	свадебная	NEW	5	5000	f	лалала	2022-04-13 14:49:48.107095+00	7	\N	8	\N
5	2022-04-17 19:00:00+00	5 часов	Свадьба	NEW	5	5000р	f	лалала	2022-04-13 16:01:10.721367+00	8	\N	7	\N
6	2022-04-17 16:02:00+00	5 часов	свадебная	NEW	5	5000р	f	лалала	2022-04-13 16:02:39.157134+00	8	\N	9	\N
7	2022-04-17 16:02:00+00	5 часов	свадебная	NEW	5	5000р	f	лалала	2022-04-13 16:03:29.666564+00	8	Парк	9	\N
8	2022-04-24 09:45:00+00	2	простая	NEW	2	3000тр	f	Просто тестовый запрос.	2022-04-14 09:46:20.665879+00	10	У дороги	9	\N
9	2022-04-18 13:51:00+00	2	new	NEW	1	12222	f	test	2022-04-18 13:51:43.359354+00	6	minsk	9	\N
10	2022-04-22 05:05:00+00	2	2	NEW	3	2	f	321	2022-04-20 04:04:45.255534+00	10	2	10	\N
11	2022-04-03 01:02:00+00	5	свадьба	NEW	5	5000	f	привет	2022-04-22 23:03:07.895111+00	7	Парк	8	\N
12	2022-04-14 23:48:00+00	5 часов	свальба	NEW	5	5000	f	ллалаа	2022-04-22 23:45:42.060886+00	8	парк	7	\N
14	2022-05-01 13:57:00+00	5часов	test	NEW	test	test	f	fdf	2022-05-01 13:57:27.205637+00	7	park	8	\N
16	2022-05-01 13:57:00+00	5часов	test	ACCEPTED	test	test	f	fdf	2022-05-01 14:06:31.300621+00	7	park	8	\N
13	2022-05-14 13:33:00+00	5часов	свадьба	ACCEPTED	5	5000	f	лалал	2022-05-01 13:33:42.80624+00	7	парк	8	\N
15	2022-05-01 13:57:00+00	5часов	test	UNCOMPLETED	test	test	f	fdf	2022-05-01 14:04:54+00	7	park	8	
17	2022-05-15 14:56:00+00	авачасов	ва	NEW	ва	вав	f	а	2022-05-01 14:56:31.425296+00	8	ва	7	\N
18	2022-04-30 14:57:00+00	аывчасов	ыва	NEW	ыва	ываы	f	ва	2022-05-01 14:57:43.442305+00	7	ыва	8	\N
19	2022-05-13 15:58:00+00	2часов	Улица	NEW	4	3000	f	Тест	2022-05-11 15:59:25.288351+00	10	Парк	7	\N
20	2022-05-14 10:00:00+00	2часов	Семейная	NEW	3	4 000	f	Здравствуйте. Рад вас приветствовать) Это тестовый запрос. Вот так вы будете видеть все запросы на съемку от пользователей :) \nХорошего дня :)	2022-05-13 10:01:49.111778+00	10	Город	15	\N
\.


--
-- Data for Name: film_places_notauthfilmrequest; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.film_places_notauthfilmrequest (id, filming_timestamp, hours_duration, filming_type, count_person, filming_budget, need_makeup_artist, description, was_added, place_filming, email, email_verify, email_code, receiver_profile_id) FROM stdin;
1	2022-05-12 12:52:00+00	5часов	свадьба	5	5000	f	sdfh	2022-05-01 13:12:39.11276+00	парк	muzhyke@gmail.com	f	KT1iFu	7
2	2022-05-07 13:17:00+00	5часов	свадьюа	5	5	f		2022-05-01 13:17:56.51771+00	парк	joffreywebd@gmail.com	f	qxX4Zk	8
\.


--
-- Data for Name: gallery_album; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_album (id, name_album, description_album, is_hidden, main_photo_id_id, profile_id) FROM stdin;
1	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	1
2	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	2
6	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	6	6
9	new album	new album	f	1	6
10	Разное	Альбом с разным	f	15	7
11	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	9
8	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	26	8
13	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	11
14	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	12
15	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	13
12	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	41	10
16	Волшебный	Наши мечты	f	45	10
18	Фоточки	описание	f	1	7
19	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	14
20	Разное	Альбом с разными фотографиями, которые не вошли в другие альбомы	f	1	15
\.


--
-- Data for Name: gallery_gallery; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_gallery (id, name_image, description, place_location, string_place_location, tags, photo_camera, focal_len, excerpt, aperture, iso, flash, is_sell, last_ip_user, views, was_added, is_hidden, gallery_image_id, profile_id) FROM stdin;
5	Фото 3	Описание	0101000020E6100000653A183DE6F44A402EA15EAB327E3B40	Беларусь, Минск	\N	фотик	тест	тест	тест	тест	тест	f	91.245.140.119	10	2022-04-08 16:14:12.433637+00	f	16	7
6	фото 4	описание	0101000020E6100000750DE92204E14B400609512ED1C54240	Россия, Москва	\N	тест	тест	тест	тест	тест	тест	f	91.245.140.119	8	2022-04-08 16:36:17.650082+00	f	17	7
3	моя фото	123	0101000020E610000017BC9201CFE04B400909512E80BC4240	Россия, Москва	\N	еуеы	еуые	ееуые	еуыеу	еуые	еуые	f	83.220.238.7	6	2022-04-07 14:37:43.959154+00	f	6	6
8	Человечек	описание	0101000020E61000001218748E88E54B400809512EC9BE4240	Россия, Москва	\N				\N	\N		f	91.245.140.119	7	2022-04-12 14:15:33.788546+00	f	26	8
17	Грузовик	Автомобиль	0101000020E610000073B1A0DA9A934B400609512E6CB54E40	Россия, Челябинск	\N				\N	\N		f	91.245.140.119	3	2022-05-10 15:05:49.032607+00	f	47	10
13	Ёлка	Ёлка	0101000020E6100000B84DC47544974A400609512E80104940	Россия, Самара	\N				\N	\N		f	91.245.140.119	3	2022-05-10 14:38:14.023561+00	f	41	10
14	Природа	Красивое место	0101000020E610000039B30C7072C94B400909516E3F064540	Россия, Владимирская область	\N	10	30	40	20	50	60	f	\N	0	2022-05-10 14:47:52.583901+00	f	44	10
4	Фото 2	описание	0101000020E61000000709512E95A7424099C73D7161E74B40	Россия, Московская область	\N	фотик	расстояние	выдержка	диафрагма	исо	вспышка	f	91.245.140.119	14	2022-04-08 16:13:24.370357+00	f	15	7
18	Котик	описание	0101000020E6100000E497F35AA7E04B400909512E2FE04240	Россия, Москва	\N	Canon Canon EOS 5D Mark II	151mm	1/400s	f/2.8	1000	Нет	f	85.143.252.35	4	2022-05-11 08:14:58.352686+00	f	48	7
15	Мишки	Семья мишек	0101000020E61000000609512E1880414003A2C9AE15C64B40	Россия, Смоленская область	\N				\N	\N		t	85.143.252.35	6	2022-05-10 14:54:21.219484+00	f	45	10
11	Котик	описание	0101000020E61000003D8FA64037E84B400709512E77C54240	Россия, Москва	\N	samsung SM-A520F	360mm	1/33s	f/1.9	80	Да	f	46.56.207.177	9	2022-04-23 07:53:09.430045+00	f	39	8
16	Лягушка	Красивое фото	0101000020E61000000B09512E22204C4046293527D1FF4C40	Россия, Пермь	\N	1	3	4	2	5	6	t	91.245.140.119	3	2022-05-10 14:56:59.532652+00	f	46	10
\.


--
-- Data for Name: gallery_gallery_album; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_gallery_album (id, gallery_id, album_id) FROM stdin;
3	3	6
5	4	10
6	5	10
7	6	10
9	8	8
12	11	8
14	13	12
15	14	12
16	15	16
17	16	16
18	17	16
19	18	10
20	18	18
21	4	18
\.


--
-- Data for Name: gallery_gallery_category; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_gallery_category (id, gallery_id, specialization_id) FROM stdin;
3	3	18
4	3	20
6	5	4
7	6	8
9	8	8
10	4	8
13	11	18
15	13	3
16	14	18
17	15	1
18	16	1
19	17	11
20	18	6
\.


--
-- Data for Name: gallery_gallerycomment; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_gallerycomment (id, content, "timestamp", answer_id_comment_id, gallery_id, quote_id_id, sender_comment_id) FROM stdin;
2	123	2022-04-07 14:38:28.706449+00	\N	3	\N	6
4	Один тест комментарий.	2022-04-09 12:56:35.868506+00	\N	5	\N	10
5	Комментарий тест	2022-04-11 07:54:30.666354+00	\N	4	\N	10
10	Красивая фоточка.	2022-05-10 14:40:35.731482+00	\N	13	\N	10
\.


--
-- Data for Name: gallery_galleryfavorite; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_galleryfavorite (id, gallery_id, profile_id) FROM stdin;
2	5	7
3	4	7
4	5	10
6	8	8
\.


--
-- Data for Name: gallery_gallerylike; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_gallerylike (id, gallery_id, profile_id) FROM stdin;
2	4	10
3	5	10
5	4	7
9	8	10
11	15	10
\.


--
-- Data for Name: gallery_image; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_image (id, photo, profile_id) FROM stdin;
1	gallery/1.jpg	1
6	gallery/6.jpg	6
7	gallery/7.jpg	7
8	gallery/7_EkrIQI7.jpg	7
9	gallery/7_fY8Qn7a.jpg	7
10	gallery/7_gaXp6wJ.jpg	7
11	gallery/7_5DCBAQ3.jpg	7
12	gallery/7_G1RjYMc.jpg	7
13	gallery/7_xF6vjoX.jpg	7
14	gallery/7_ZyOzser.jpg	7
15	gallery/7_Rn12tS5.jpg	7
16	gallery/7_RhxWv14.jpg	7
17	gallery/7_3ey38vl.jpg	7
18	gallery/10.jpg	10
20	gallery/10_nTYH4oH.jpg	10
21	gallery/10_luEnkX8.jpg	10
22	gallery/10_wvArygR.jpg	10
23	gallery/10_UDRxY2e.jpg	10
24	gallery/10_su33M4w.jpg	10
25	gallery/10_4VBBT2e.jpg	10
26	gallery/8.jpg	8
29	gallery/7_U5IE8EK.jpg	7
30	gallery/7_UWd6Zpx.jpg	7
31	gallery/7_W4xLyfb.jpg	7
32	gallery/7_ma8ge4g.jpg	7
33	gallery/10_v4rcQgx.jpg	10
34	gallery/10_nSBD5VO.jpg	10
35	gallery/10_tTf2vdM.jpg	10
36	gallery/10_EwCNHvO.jpg	10
37	gallery/10_QoDjQOU.jpg	10
38	gallery/10_EYQibka.jpg	10
39	gallery/8_APWcEKV.jpg	8
41	gallery/10_XOis6zI.jpg	10
42	gallery/10_gkEieBs.jpg	10
43	gallery/10_4cLmi9e.jpg	10
44	gallery/10_bgyhCU2.jpg	10
45	gallery/10_gyf6gNJ.jpg	10
46	gallery/10_2TBXkSa.jpg	10
47	gallery/10_ZSMuLP0.jpg	10
48	gallery/7_IFkGJJW.jpg	7
49	gallery/10_ohdtZpc.jpg	10
50	gallery/10_6aDRGXJ.jpg	10
51	gallery/10_YJ8VEeD.jpg	10
52	gallery/10_yr4ylVq.jpg	10
53	gallery/15.jpg	15
54	gallery/15_kreRgvC.jpg	15
55	gallery/15_snX03yL.jpg	15
56	gallery/15_MEIgZPq.jpg	15
57	gallery/15_MaC0tsm.jpg	15
58	gallery/15_4vZmlph.jpg	15
\.


--
-- Data for Name: gallery_photosession; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_photosession (id, session_name, session_description, session_location, string_session_location, session_date, last_ip_user, views, is_hidden, main_photo_id, profile_id, session_category_id) FROM stdin;
1	Сессия 1	Описание	0101000020E6100000DCFECB5BF8E44B400909512E7FCC4240	Россия, Москва	2022-04-14	91.149.129.124	7	f	12	7	\N
3	Прогулочная фотосессия 15 минут	Прогулка на закате по центру города	0101000020E6100000EDB390D912834B40C31EE0FA2EBB5440	Россия, Новосибирск	2022-05-13	5.130.138.210	1	f	53	15	\N
\.


--
-- Data for Name: gallery_photosession_photos; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_photosession_photos (id, photosession_id, image_id) FROM stdin;
1	1	11
2	1	12
3	1	13
4	1	14
11	3	53
12	3	54
13	3	55
14	3	56
15	3	57
16	3	58
\.


--
-- Data for Name: gallery_photosessioncomment; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_photosessioncomment (id, content, "timestamp", answer_id_comment_id, photo_session_id, quote_id_id, sender_comment_id) FROM stdin;
\.


--
-- Data for Name: gallery_photosessionfavorite; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_photosessionfavorite (id, photo_session_id, profile_id) FROM stdin;
1	1	7
\.


--
-- Data for Name: gallery_photosessionlike; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.gallery_photosessionlike (id, photo_session_id, profile_id) FROM stdin;
1	1	7
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: photo_user
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: topology; Type: TABLE DATA; Schema: topology; Owner: photo_user
--

COPY topology.topology (id, name, srid, "precision", hasz) FROM stdin;
\.


--
-- Data for Name: layer; Type: TABLE DATA; Schema: topology; Owner: photo_user
--

COPY topology.layer (topology_id, layer_id, schema_name, table_name, feature_column, feature_type, level, child_id) FROM stdin;
\.


--
-- Name: accounts_procategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_procategory_id_seq', 11, true);


--
-- Name: accounts_profile_filming_geo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profile_filming_geo_id_seq', 5, true);


--
-- Name: accounts_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profile_id_seq', 15, true);


--
-- Name: accounts_profile_languages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profile_languages_id_seq', 6, true);


--
-- Name: accounts_profile_spec_model_or_photographer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profile_spec_model_or_photographer_id_seq', 7, true);


--
-- Name: accounts_profilecomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profilecomment_id_seq', 1, false);


--
-- Name: accounts_profilefavorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profilefavorite_id_seq', 6, true);


--
-- Name: accounts_profilelike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_profilelike_id_seq', 1, false);


--
-- Name: accounts_specialization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_specialization_id_seq', 20, true);


--
-- Name: accounts_verificationcode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.accounts_verificationcode_id_seq', 15, true);


--
-- Name: additional_entities_advertisement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_advertisement_id_seq', 1, true);


--
-- Name: additional_entities_answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_answer_id_seq', 1, false);


--
-- Name: additional_entities_banword_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_banword_id_seq', 340, true);


--
-- Name: additional_entities_choice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_choice_id_seq', 1, false);


--
-- Name: additional_entities_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_city_id_seq', 1243, true);


--
-- Name: additional_entities_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_country_id_seq', 202, true);


--
-- Name: additional_entities_customsettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_customsettings_id_seq', 1, true);


--
-- Name: additional_entities_emailfragment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_emailfragment_id_seq', 1, true);


--
-- Name: additional_entities_language_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_language_id_seq', 6, true);


--
-- Name: additional_entities_question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.additional_entities_question_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 180, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 15, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: chat_chat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.chat_chat_id_seq', 10, true);


--
-- Name: chat_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.chat_message_id_seq', 114, true);


--
-- Name: chat_notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.chat_notification_id_seq', 1, false);


--
-- Name: chat_requestchat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.chat_requestchat_id_seq', 19, true);


--
-- Name: chat_requestmessage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.chat_requestmessage_id_seq', 32, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 126, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 45, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 39, true);


--
-- Name: film_places_categoryfilmplaces_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_categoryfilmplaces_id_seq', 17, true);


--
-- Name: film_places_filmplaces_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplaces_category_id_seq', 8, true);


--
-- Name: film_places_filmplaces_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplaces_id_seq', 8, true);


--
-- Name: film_places_filmplaces_place_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplaces_place_image_id_seq', 18, true);


--
-- Name: film_places_filmplacescomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplacescomment_id_seq', 1, false);


--
-- Name: film_places_filmplacesfavorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplacesfavorite_id_seq', 2, true);


--
-- Name: film_places_filmplaceslike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmplaceslike_id_seq', 1, false);


--
-- Name: film_places_filmrequest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_filmrequest_id_seq', 20, true);


--
-- Name: film_places_notauthfilmrequest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.film_places_notauthfilmrequest_id_seq', 2, true);


--
-- Name: gallery_album_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_album_id_seq', 20, true);


--
-- Name: gallery_gallery_album_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_gallery_album_id_seq', 22, true);


--
-- Name: gallery_gallery_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_gallery_category_id_seq', 20, true);


--
-- Name: gallery_gallery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_gallery_id_seq', 18, true);


--
-- Name: gallery_gallerycomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_gallerycomment_id_seq', 10, true);


--
-- Name: gallery_galleryfavorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_galleryfavorite_id_seq', 6, true);


--
-- Name: gallery_gallerylike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_gallerylike_id_seq', 11, true);


--
-- Name: gallery_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_image_id_seq', 58, true);


--
-- Name: gallery_photosession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_photosession_id_seq', 3, true);


--
-- Name: gallery_photosession_photos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_photosession_photos_id_seq', 16, true);


--
-- Name: gallery_photosessioncomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_photosessioncomment_id_seq', 1, false);


--
-- Name: gallery_photosessionfavorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_photosessionfavorite_id_seq', 1, true);


--
-- Name: gallery_photosessionlike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: photo_user
--

SELECT pg_catalog.setval('public.gallery_photosessionlike_id_seq', 1, true);


--
-- Name: accounts_procategory accounts_procategory_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_procategory
    ADD CONSTRAINT accounts_procategory_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile_filming_geo accounts_profile_filming_geo_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_filming_geo
    ADD CONSTRAINT accounts_profile_filming_geo_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile_filming_geo accounts_profile_filming_profile_id_country_id_84a559a0_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_filming_geo
    ADD CONSTRAINT accounts_profile_filming_profile_id_country_id_84a559a0_uniq UNIQUE (profile_id, country_id);


--
-- Name: accounts_profile_languages accounts_profile_languages_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_languages
    ADD CONSTRAINT accounts_profile_languages_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile_languages accounts_profile_languages_profile_id_language_id_48036091_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_languages
    ADD CONSTRAINT accounts_profile_languages_profile_id_language_id_48036091_uniq UNIQUE (profile_id, language_id);


--
-- Name: accounts_profile accounts_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile
    ADD CONSTRAINT accounts_profile_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile_spec_model_or_photographer accounts_profile_spec_mo_profile_id_specializatio_5c9dbdda_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_spec_model_or_photographer
    ADD CONSTRAINT accounts_profile_spec_mo_profile_id_specializatio_5c9dbdda_uniq UNIQUE (profile_id, specialization_id);


--
-- Name: accounts_profile_spec_model_or_photographer accounts_profile_spec_model_or_photographer_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_spec_model_or_photographer
    ADD CONSTRAINT accounts_profile_spec_model_or_photographer_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile accounts_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile
    ADD CONSTRAINT accounts_profile_user_id_key UNIQUE (user_id);


--
-- Name: accounts_profilecomment accounts_profilecomment_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment
    ADD CONSTRAINT accounts_profilecomment_pkey PRIMARY KEY (id);


--
-- Name: accounts_profilefavorite accounts_profilefavorite_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilefavorite
    ADD CONSTRAINT accounts_profilefavorite_pkey PRIMARY KEY (id);


--
-- Name: accounts_profilelike accounts_profilelike_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilelike
    ADD CONSTRAINT accounts_profilelike_pkey PRIMARY KEY (id);


--
-- Name: accounts_specialization accounts_specialization_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_specialization
    ADD CONSTRAINT accounts_specialization_pkey PRIMARY KEY (id);


--
-- Name: accounts_verificationcode accounts_verificationcode_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_verificationcode
    ADD CONSTRAINT accounts_verificationcode_pkey PRIMARY KEY (id);


--
-- Name: accounts_verificationcode accounts_verificationcode_profile_id_id_key; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_verificationcode
    ADD CONSTRAINT accounts_verificationcode_profile_id_id_key UNIQUE (profile_id_id);


--
-- Name: additional_entities_advertisement additional_entities_advertisement_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_advertisement
    ADD CONSTRAINT additional_entities_advertisement_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_answer additional_entities_answer_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_answer
    ADD CONSTRAINT additional_entities_answer_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_banword additional_entities_banword_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_banword
    ADD CONSTRAINT additional_entities_banword_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_choice additional_entities_choice_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_choice
    ADD CONSTRAINT additional_entities_choice_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_city additional_entities_city_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_city
    ADD CONSTRAINT additional_entities_city_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_country additional_entities_country_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_country
    ADD CONSTRAINT additional_entities_country_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_customsettings additional_entities_customsettings_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_customsettings
    ADD CONSTRAINT additional_entities_customsettings_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_emailfragment additional_entities_emailfragment_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_emailfragment
    ADD CONSTRAINT additional_entities_emailfragment_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_language additional_entities_language_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_language
    ADD CONSTRAINT additional_entities_language_pkey PRIMARY KEY (id);


--
-- Name: additional_entities_question additional_entities_question_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_question
    ADD CONSTRAINT additional_entities_question_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: chat_chat chat_chat_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_chat
    ADD CONSTRAINT chat_chat_pkey PRIMARY KEY (id);


--
-- Name: chat_message chat_message_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_message
    ADD CONSTRAINT chat_message_pkey PRIMARY KEY (id);


--
-- Name: chat_notification chat_notification_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_notification
    ADD CONSTRAINT chat_notification_pkey PRIMARY KEY (id);


--
-- Name: chat_requestchat chat_requestchat_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestchat
    ADD CONSTRAINT chat_requestchat_pkey PRIMARY KEY (id);


--
-- Name: chat_requestmessage chat_requestmessage_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestmessage
    ADD CONSTRAINT chat_requestmessage_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: film_places_categoryfilmplaces film_places_categoryfilmplaces_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_categoryfilmplaces
    ADD CONSTRAINT film_places_categoryfilmplaces_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplaces_category film_places_filmplaces_c_filmplaces_id_categoryfi_3a4aeb9c_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_category
    ADD CONSTRAINT film_places_filmplaces_c_filmplaces_id_categoryfi_3a4aeb9c_uniq UNIQUE (filmplaces_id, categoryfilmplaces_id);


--
-- Name: film_places_filmplaces_category film_places_filmplaces_category_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_category
    ADD CONSTRAINT film_places_filmplaces_category_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplaces_place_image film_places_filmplaces_p_filmplaces_id_image_id_a1e2b702_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_place_image
    ADD CONSTRAINT film_places_filmplaces_p_filmplaces_id_image_id_a1e2b702_uniq UNIQUE (filmplaces_id, image_id);


--
-- Name: film_places_filmplaces film_places_filmplaces_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces
    ADD CONSTRAINT film_places_filmplaces_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplaces_place_image film_places_filmplaces_place_image_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_place_image
    ADD CONSTRAINT film_places_filmplaces_place_image_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplacescomment film_places_filmplacescomment_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment
    ADD CONSTRAINT film_places_filmplacescomment_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplacesfavorite film_places_filmplacesfavorite_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacesfavorite
    ADD CONSTRAINT film_places_filmplacesfavorite_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmplaceslike film_places_filmplaceslike_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaceslike
    ADD CONSTRAINT film_places_filmplaceslike_pkey PRIMARY KEY (id);


--
-- Name: film_places_filmrequest film_places_filmrequest_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmrequest
    ADD CONSTRAINT film_places_filmrequest_pkey PRIMARY KEY (id);


--
-- Name: film_places_notauthfilmrequest film_places_notauthfilmrequest_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_notauthfilmrequest
    ADD CONSTRAINT film_places_notauthfilmrequest_pkey PRIMARY KEY (id);


--
-- Name: gallery_album gallery_album_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_album
    ADD CONSTRAINT gallery_album_pkey PRIMARY KEY (id);


--
-- Name: gallery_gallery_album gallery_gallery_album_gallery_id_album_id_f491a05d_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_album
    ADD CONSTRAINT gallery_gallery_album_gallery_id_album_id_f491a05d_uniq UNIQUE (gallery_id, album_id);


--
-- Name: gallery_gallery_album gallery_gallery_album_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_album
    ADD CONSTRAINT gallery_gallery_album_pkey PRIMARY KEY (id);


--
-- Name: gallery_gallery_category gallery_gallery_category_gallery_id_specializatio_a7c6f9bd_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_category
    ADD CONSTRAINT gallery_gallery_category_gallery_id_specializatio_a7c6f9bd_uniq UNIQUE (gallery_id, specialization_id);


--
-- Name: gallery_gallery_category gallery_gallery_category_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_category
    ADD CONSTRAINT gallery_gallery_category_pkey PRIMARY KEY (id);


--
-- Name: gallery_gallery gallery_gallery_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery
    ADD CONSTRAINT gallery_gallery_pkey PRIMARY KEY (id);


--
-- Name: gallery_gallerycomment gallery_gallerycomment_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment
    ADD CONSTRAINT gallery_gallerycomment_pkey PRIMARY KEY (id);


--
-- Name: gallery_galleryfavorite gallery_galleryfavorite_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_galleryfavorite
    ADD CONSTRAINT gallery_galleryfavorite_pkey PRIMARY KEY (id);


--
-- Name: gallery_gallerylike gallery_gallerylike_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerylike
    ADD CONSTRAINT gallery_gallerylike_pkey PRIMARY KEY (id);


--
-- Name: gallery_image gallery_image_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_image
    ADD CONSTRAINT gallery_image_pkey PRIMARY KEY (id);


--
-- Name: gallery_photosession_photos gallery_photosession_pho_photosession_id_image_id_f27258cb_uniq; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession_photos
    ADD CONSTRAINT gallery_photosession_pho_photosession_id_image_id_f27258cb_uniq UNIQUE (photosession_id, image_id);


--
-- Name: gallery_photosession_photos gallery_photosession_photos_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession_photos
    ADD CONSTRAINT gallery_photosession_photos_pkey PRIMARY KEY (id);


--
-- Name: gallery_photosession gallery_photosession_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession
    ADD CONSTRAINT gallery_photosession_pkey PRIMARY KEY (id);


--
-- Name: gallery_photosessioncomment gallery_photosessioncomment_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment
    ADD CONSTRAINT gallery_photosessioncomment_pkey PRIMARY KEY (id);


--
-- Name: gallery_photosessionfavorite gallery_photosessionfavorite_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionfavorite
    ADD CONSTRAINT gallery_photosessionfavorite_pkey PRIMARY KEY (id);


--
-- Name: gallery_photosessionlike gallery_photosessionlike_pkey; Type: CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionlike
    ADD CONSTRAINT gallery_photosessionlike_pkey PRIMARY KEY (id);


--
-- Name: accounts_profile_filming_geo_country_id_69c5f409; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_filming_geo_country_id_69c5f409 ON public.accounts_profile_filming_geo USING btree (country_id);


--
-- Name: accounts_profile_filming_geo_profile_id_07d74e64; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_filming_geo_profile_id_07d74e64 ON public.accounts_profile_filming_geo USING btree (profile_id);


--
-- Name: accounts_profile_languages_language_id_194609ba; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_languages_language_id_194609ba ON public.accounts_profile_languages USING btree (language_id);


--
-- Name: accounts_profile_languages_profile_id_eabf6019; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_languages_profile_id_eabf6019 ON public.accounts_profile_languages USING btree (profile_id);


--
-- Name: accounts_profile_location_id; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_location_id ON public.accounts_profile USING gist (location);


--
-- Name: accounts_profile_location_now_id; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_location_now_id ON public.accounts_profile USING gist (location_now);


--
-- Name: accounts_profile_spec_mode_specialization_id_9447e3ca; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_spec_mode_specialization_id_9447e3ca ON public.accounts_profile_spec_model_or_photographer USING btree (specialization_id);


--
-- Name: accounts_profile_spec_model_or_photographer_profile_id_398c5f8c; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_spec_model_or_photographer_profile_id_398c5f8c ON public.accounts_profile_spec_model_or_photographer USING btree (profile_id);


--
-- Name: accounts_profile_type_pro_id_ecebbef4; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profile_type_pro_id_ecebbef4 ON public.accounts_profile USING btree (type_pro_id);


--
-- Name: accounts_profilecomment_answer_id_comment_id_94e029a6; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilecomment_answer_id_comment_id_94e029a6 ON public.accounts_profilecomment USING btree (answer_id_comment_id);


--
-- Name: accounts_profilecomment_quote_id_id_0599138f; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilecomment_quote_id_id_0599138f ON public.accounts_profilecomment USING btree (quote_id_id);


--
-- Name: accounts_profilecomment_receiver_comment_id_40484f8d; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilecomment_receiver_comment_id_40484f8d ON public.accounts_profilecomment USING btree (receiver_comment_id);


--
-- Name: accounts_profilecomment_sender_comment_id_8d7dfacf; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilecomment_sender_comment_id_8d7dfacf ON public.accounts_profilecomment USING btree (sender_comment_id);


--
-- Name: accounts_profilefavorite_receiver_favorite_id_cc214602; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilefavorite_receiver_favorite_id_cc214602 ON public.accounts_profilefavorite USING btree (receiver_favorite_id);


--
-- Name: accounts_profilefavorite_sender_favorite_id_12ba9e48; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilefavorite_sender_favorite_id_12ba9e48 ON public.accounts_profilefavorite USING btree (sender_favorite_id);


--
-- Name: accounts_profilelike_receiver_like_id_603d1d7b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilelike_receiver_like_id_603d1d7b ON public.accounts_profilelike USING btree (receiver_like_id);


--
-- Name: accounts_profilelike_sender_like_id_5c3f186e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX accounts_profilelike_sender_like_id_5c3f186e ON public.accounts_profilelike USING btree (sender_like_id);


--
-- Name: additional_entities_answer_choice_id_40341638; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX additional_entities_answer_choice_id_40341638 ON public.additional_entities_answer USING btree (choice_id);


--
-- Name: additional_entities_answer_profile_id_c5f2b2ff; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX additional_entities_answer_profile_id_c5f2b2ff ON public.additional_entities_answer USING btree (profile_id);


--
-- Name: additional_entities_choice_question_id_640debf5; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX additional_entities_choice_question_id_640debf5 ON public.additional_entities_choice USING btree (question_id);


--
-- Name: additional_entities_city_country_id_9dfd27c3; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX additional_entities_city_country_id_9dfd27c3 ON public.additional_entities_city USING btree (country_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: chat_chat_receiver_id_id_62940e3f; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_chat_receiver_id_id_62940e3f ON public.chat_chat USING btree (receiver_id_id);


--
-- Name: chat_chat_sender_id_id_f067d315; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_chat_sender_id_id_f067d315 ON public.chat_chat USING btree (sender_id_id);


--
-- Name: chat_message_author_id_923569d5; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_message_author_id_923569d5 ON public.chat_message USING btree (author_id);


--
-- Name: chat_message_chat_id_21483fa7; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_message_chat_id_21483fa7 ON public.chat_message USING btree (chat_id);


--
-- Name: chat_notification_receiver_id_c26646d2; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_notification_receiver_id_c26646d2 ON public.chat_notification USING btree (receiver_id);


--
-- Name: chat_notification_sender_id_f9d5a6c6; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_notification_sender_id_f9d5a6c6 ON public.chat_notification USING btree (sender_id);


--
-- Name: chat_requestchat_request_receiver_id_7f549032; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_requestchat_request_receiver_id_7f549032 ON public.chat_requestchat USING btree (request_receiver_id);


--
-- Name: chat_requestchat_request_sender_id_209eb682; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_requestchat_request_sender_id_209eb682 ON public.chat_requestchat USING btree (request_sender_id);


--
-- Name: chat_requestmessage_author_id_7d2749dd; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_requestmessage_author_id_7d2749dd ON public.chat_requestmessage USING btree (author_id);


--
-- Name: chat_requestmessage_chat_id_54aa98af; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_requestmessage_chat_id_54aa98af ON public.chat_requestmessage USING btree (chat_id);


--
-- Name: chat_requestmessage_request_id_2d05494c; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX chat_requestmessage_request_id_2d05494c ON public.chat_requestmessage USING btree (request_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: film_places_filmplaces_category_categoryfilmplaces_id_d3a28e0e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_category_categoryfilmplaces_id_d3a28e0e ON public.film_places_filmplaces_category USING btree (categoryfilmplaces_id);


--
-- Name: film_places_filmplaces_category_filmplaces_id_3e85da19; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_category_filmplaces_id_3e85da19 ON public.film_places_filmplaces_category USING btree (filmplaces_id);


--
-- Name: film_places_filmplaces_main_photo_id_9cf1199a; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_main_photo_id_9cf1199a ON public.film_places_filmplaces USING btree (main_photo_id);


--
-- Name: film_places_filmplaces_place_image_filmplaces_id_4c4a2cb3; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_place_image_filmplaces_id_4c4a2cb3 ON public.film_places_filmplaces_place_image USING btree (filmplaces_id);


--
-- Name: film_places_filmplaces_place_image_image_id_986da258; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_place_image_image_id_986da258 ON public.film_places_filmplaces_place_image USING btree (image_id);


--
-- Name: film_places_filmplaces_place_location_id; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_place_location_id ON public.film_places_filmplaces USING gist (place_location);


--
-- Name: film_places_filmplaces_profile_id_3aaf61f0; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaces_profile_id_3aaf61f0 ON public.film_places_filmplaces USING btree (profile_id);


--
-- Name: film_places_filmplacescomment_answer_id_comment_id_82f3d057; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacescomment_answer_id_comment_id_82f3d057 ON public.film_places_filmplacescomment USING btree (answer_id_comment_id);


--
-- Name: film_places_filmplacescomment_place_id_3dcaf5ac; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacescomment_place_id_3dcaf5ac ON public.film_places_filmplacescomment USING btree (place_id);


--
-- Name: film_places_filmplacescomment_quote_id_id_fe7944ef; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacescomment_quote_id_id_fe7944ef ON public.film_places_filmplacescomment USING btree (quote_id_id);


--
-- Name: film_places_filmplacescomment_sender_comment_id_061c4cd3; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacescomment_sender_comment_id_061c4cd3 ON public.film_places_filmplacescomment USING btree (sender_comment_id);


--
-- Name: film_places_filmplacesfavorite_place_id_ba240d62; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacesfavorite_place_id_ba240d62 ON public.film_places_filmplacesfavorite USING btree (place_id);


--
-- Name: film_places_filmplacesfavorite_profile_id_94c8a44e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplacesfavorite_profile_id_94c8a44e ON public.film_places_filmplacesfavorite USING btree (profile_id);


--
-- Name: film_places_filmplaceslike_place_id_6ad4769d; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaceslike_place_id_6ad4769d ON public.film_places_filmplaceslike USING btree (place_id);


--
-- Name: film_places_filmplaceslike_profile_id_07af7f5f; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmplaceslike_profile_id_07af7f5f ON public.film_places_filmplaceslike USING btree (profile_id);


--
-- Name: film_places_filmrequest_profile_id_da6efa18; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmrequest_profile_id_da6efa18 ON public.film_places_filmrequest USING btree (profile_id);


--
-- Name: film_places_filmrequest_receiver_profile_id_eeb13afe; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_filmrequest_receiver_profile_id_eeb13afe ON public.film_places_filmrequest USING btree (receiver_profile_id);


--
-- Name: film_places_notauthfilmrequest_receiver_profile_id_1fa89e32; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX film_places_notauthfilmrequest_receiver_profile_id_1fa89e32 ON public.film_places_notauthfilmrequest USING btree (receiver_profile_id);


--
-- Name: gallery_album_main_photo_id_id_b28832d5; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_album_main_photo_id_id_b28832d5 ON public.gallery_album USING btree (main_photo_id_id);


--
-- Name: gallery_album_profile_id_bd3955ac; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_album_profile_id_bd3955ac ON public.gallery_album USING btree (profile_id);


--
-- Name: gallery_gallery_album_album_id_6eda7942; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_album_album_id_6eda7942 ON public.gallery_gallery_album USING btree (album_id);


--
-- Name: gallery_gallery_album_gallery_id_35e407e4; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_album_gallery_id_35e407e4 ON public.gallery_gallery_album USING btree (gallery_id);


--
-- Name: gallery_gallery_category_gallery_id_5533916e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_category_gallery_id_5533916e ON public.gallery_gallery_category USING btree (gallery_id);


--
-- Name: gallery_gallery_category_specialization_id_63cf984f; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_category_specialization_id_63cf984f ON public.gallery_gallery_category USING btree (specialization_id);


--
-- Name: gallery_gallery_gallery_image_id_0fd2be9f; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_gallery_image_id_0fd2be9f ON public.gallery_gallery USING btree (gallery_image_id);


--
-- Name: gallery_gallery_place_location_id; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_place_location_id ON public.gallery_gallery USING gist (place_location);


--
-- Name: gallery_gallery_profile_id_f7b1a984; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallery_profile_id_f7b1a984 ON public.gallery_gallery USING btree (profile_id);


--
-- Name: gallery_gallerycomment_answer_id_comment_id_aa8ae339; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerycomment_answer_id_comment_id_aa8ae339 ON public.gallery_gallerycomment USING btree (answer_id_comment_id);


--
-- Name: gallery_gallerycomment_gallery_id_80df8aba; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerycomment_gallery_id_80df8aba ON public.gallery_gallerycomment USING btree (gallery_id);


--
-- Name: gallery_gallerycomment_quote_id_id_ef5aba5b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerycomment_quote_id_id_ef5aba5b ON public.gallery_gallerycomment USING btree (quote_id_id);


--
-- Name: gallery_gallerycomment_sender_comment_id_e72e5ac6; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerycomment_sender_comment_id_e72e5ac6 ON public.gallery_gallerycomment USING btree (sender_comment_id);


--
-- Name: gallery_galleryfavorite_gallery_id_bccfcafc; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_galleryfavorite_gallery_id_bccfcafc ON public.gallery_galleryfavorite USING btree (gallery_id);


--
-- Name: gallery_galleryfavorite_profile_id_4ad1ef4b; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_galleryfavorite_profile_id_4ad1ef4b ON public.gallery_galleryfavorite USING btree (profile_id);


--
-- Name: gallery_gallerylike_gallery_id_6b9da5a3; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerylike_gallery_id_6b9da5a3 ON public.gallery_gallerylike USING btree (gallery_id);


--
-- Name: gallery_gallerylike_profile_id_4980571a; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_gallerylike_profile_id_4980571a ON public.gallery_gallerylike USING btree (profile_id);


--
-- Name: gallery_image_profile_id_0afef851; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_image_profile_id_0afef851 ON public.gallery_image USING btree (profile_id);


--
-- Name: gallery_photosession_main_photo_id_dddb8bef; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_main_photo_id_dddb8bef ON public.gallery_photosession USING btree (main_photo_id);


--
-- Name: gallery_photosession_photos_image_id_651652cd; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_photos_image_id_651652cd ON public.gallery_photosession_photos USING btree (image_id);


--
-- Name: gallery_photosession_photos_photosession_id_83c87951; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_photos_photosession_id_83c87951 ON public.gallery_photosession_photos USING btree (photosession_id);


--
-- Name: gallery_photosession_profile_id_96e6036e; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_profile_id_96e6036e ON public.gallery_photosession USING btree (profile_id);


--
-- Name: gallery_photosession_session_category_id_0ca02969; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_session_category_id_0ca02969 ON public.gallery_photosession USING btree (session_category_id);


--
-- Name: gallery_photosession_session_location_id; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosession_session_location_id ON public.gallery_photosession USING gist (session_location);


--
-- Name: gallery_photosessioncomment_answer_id_comment_id_0570198c; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessioncomment_answer_id_comment_id_0570198c ON public.gallery_photosessioncomment USING btree (answer_id_comment_id);


--
-- Name: gallery_photosessioncomment_photo_session_id_d4b5267d; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessioncomment_photo_session_id_d4b5267d ON public.gallery_photosessioncomment USING btree (photo_session_id);


--
-- Name: gallery_photosessioncomment_quote_id_id_b2241806; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessioncomment_quote_id_id_b2241806 ON public.gallery_photosessioncomment USING btree (quote_id_id);


--
-- Name: gallery_photosessioncomment_sender_comment_id_97d27382; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessioncomment_sender_comment_id_97d27382 ON public.gallery_photosessioncomment USING btree (sender_comment_id);


--
-- Name: gallery_photosessionfavorite_photo_session_id_fed07a7d; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessionfavorite_photo_session_id_fed07a7d ON public.gallery_photosessionfavorite USING btree (photo_session_id);


--
-- Name: gallery_photosessionfavorite_profile_id_6acb43c2; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessionfavorite_profile_id_6acb43c2 ON public.gallery_photosessionfavorite USING btree (profile_id);


--
-- Name: gallery_photosessionlike_photo_session_id_3ae0d312; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessionlike_photo_session_id_3ae0d312 ON public.gallery_photosessionlike USING btree (photo_session_id);


--
-- Name: gallery_photosessionlike_profile_id_cf5c3f32; Type: INDEX; Schema: public; Owner: photo_user
--

CREATE INDEX gallery_photosessionlike_profile_id_cf5c3f32 ON public.gallery_photosessionlike USING btree (profile_id);


--
-- Name: accounts_profile_filming_geo accounts_profile_fil_country_id_69c5f409_fk_additiona; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_filming_geo
    ADD CONSTRAINT accounts_profile_fil_country_id_69c5f409_fk_additiona FOREIGN KEY (country_id) REFERENCES public.additional_entities_country(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile_filming_geo accounts_profile_fil_profile_id_07d74e64_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_filming_geo
    ADD CONSTRAINT accounts_profile_fil_profile_id_07d74e64_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile_languages accounts_profile_lan_language_id_194609ba_fk_additiona; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_languages
    ADD CONSTRAINT accounts_profile_lan_language_id_194609ba_fk_additiona FOREIGN KEY (language_id) REFERENCES public.additional_entities_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile_languages accounts_profile_lan_profile_id_eabf6019_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_languages
    ADD CONSTRAINT accounts_profile_lan_profile_id_eabf6019_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile_spec_model_or_photographer accounts_profile_spe_profile_id_398c5f8c_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_spec_model_or_photographer
    ADD CONSTRAINT accounts_profile_spe_profile_id_398c5f8c_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile_spec_model_or_photographer accounts_profile_spe_specialization_id_9447e3ca_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile_spec_model_or_photographer
    ADD CONSTRAINT accounts_profile_spe_specialization_id_9447e3ca_fk_accounts_ FOREIGN KEY (specialization_id) REFERENCES public.accounts_specialization(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile accounts_profile_type_pro_id_ecebbef4_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile
    ADD CONSTRAINT accounts_profile_type_pro_id_ecebbef4_fk_accounts_ FOREIGN KEY (type_pro_id) REFERENCES public.accounts_procategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profile accounts_profile_user_id_49a85d32_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profile
    ADD CONSTRAINT accounts_profile_user_id_49a85d32_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilecomment accounts_profilecomm_answer_id_comment_id_94e029a6_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment
    ADD CONSTRAINT accounts_profilecomm_answer_id_comment_id_94e029a6_fk_accounts_ FOREIGN KEY (answer_id_comment_id) REFERENCES public.accounts_profilecomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilecomment accounts_profilecomm_quote_id_id_0599138f_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment
    ADD CONSTRAINT accounts_profilecomm_quote_id_id_0599138f_fk_accounts_ FOREIGN KEY (quote_id_id) REFERENCES public.accounts_profilecomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilecomment accounts_profilecomm_receiver_comment_id_40484f8d_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment
    ADD CONSTRAINT accounts_profilecomm_receiver_comment_id_40484f8d_fk_accounts_ FOREIGN KEY (receiver_comment_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilecomment accounts_profilecomm_sender_comment_id_8d7dfacf_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilecomment
    ADD CONSTRAINT accounts_profilecomm_sender_comment_id_8d7dfacf_fk_accounts_ FOREIGN KEY (sender_comment_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilefavorite accounts_profilefavo_receiver_favorite_id_cc214602_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilefavorite
    ADD CONSTRAINT accounts_profilefavo_receiver_favorite_id_cc214602_fk_accounts_ FOREIGN KEY (receiver_favorite_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilefavorite accounts_profilefavo_sender_favorite_id_12ba9e48_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilefavorite
    ADD CONSTRAINT accounts_profilefavo_sender_favorite_id_12ba9e48_fk_accounts_ FOREIGN KEY (sender_favorite_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilelike accounts_profilelike_receiver_like_id_603d1d7b_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilelike
    ADD CONSTRAINT accounts_profilelike_receiver_like_id_603d1d7b_fk_accounts_ FOREIGN KEY (receiver_like_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_profilelike accounts_profilelike_sender_like_id_5c3f186e_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_profilelike
    ADD CONSTRAINT accounts_profilelike_sender_like_id_5c3f186e_fk_accounts_ FOREIGN KEY (sender_like_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_verificationcode accounts_verificatio_profile_id_id_6c67807b_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.accounts_verificationcode
    ADD CONSTRAINT accounts_verificatio_profile_id_id_6c67807b_fk_accounts_ FOREIGN KEY (profile_id_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: additional_entities_answer additional_entities__choice_id_40341638_fk_additiona; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_answer
    ADD CONSTRAINT additional_entities__choice_id_40341638_fk_additiona FOREIGN KEY (choice_id) REFERENCES public.additional_entities_choice(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: additional_entities_city additional_entities__country_id_9dfd27c3_fk_additiona; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_city
    ADD CONSTRAINT additional_entities__country_id_9dfd27c3_fk_additiona FOREIGN KEY (country_id) REFERENCES public.additional_entities_country(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: additional_entities_answer additional_entities__profile_id_c5f2b2ff_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_answer
    ADD CONSTRAINT additional_entities__profile_id_c5f2b2ff_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: additional_entities_choice additional_entities__question_id_640debf5_fk_additiona; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.additional_entities_choice
    ADD CONSTRAINT additional_entities__question_id_640debf5_fk_additiona FOREIGN KEY (question_id) REFERENCES public.additional_entities_question(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_chat chat_chat_receiver_id_id_62940e3f_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_chat
    ADD CONSTRAINT chat_chat_receiver_id_id_62940e3f_fk_accounts_profile_id FOREIGN KEY (receiver_id_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_chat chat_chat_sender_id_id_f067d315_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_chat
    ADD CONSTRAINT chat_chat_sender_id_id_f067d315_fk_accounts_profile_id FOREIGN KEY (sender_id_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_message chat_message_author_id_923569d5_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_message
    ADD CONSTRAINT chat_message_author_id_923569d5_fk_accounts_profile_id FOREIGN KEY (author_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_message chat_message_chat_id_21483fa7_fk_chat_chat_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_message
    ADD CONSTRAINT chat_message_chat_id_21483fa7_fk_chat_chat_id FOREIGN KEY (chat_id) REFERENCES public.chat_chat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_notification chat_notification_receiver_id_c26646d2_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_notification
    ADD CONSTRAINT chat_notification_receiver_id_c26646d2_fk_accounts_profile_id FOREIGN KEY (receiver_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_notification chat_notification_sender_id_f9d5a6c6_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_notification
    ADD CONSTRAINT chat_notification_sender_id_f9d5a6c6_fk_accounts_profile_id FOREIGN KEY (sender_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_requestchat chat_requestchat_request_receiver_id_7f549032_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestchat
    ADD CONSTRAINT chat_requestchat_request_receiver_id_7f549032_fk_accounts_ FOREIGN KEY (request_receiver_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_requestchat chat_requestchat_request_sender_id_209eb682_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestchat
    ADD CONSTRAINT chat_requestchat_request_sender_id_209eb682_fk_accounts_ FOREIGN KEY (request_sender_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_requestmessage chat_requestmessage_author_id_7d2749dd_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestmessage
    ADD CONSTRAINT chat_requestmessage_author_id_7d2749dd_fk_accounts_profile_id FOREIGN KEY (author_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_requestmessage chat_requestmessage_chat_id_54aa98af_fk_chat_requestchat_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestmessage
    ADD CONSTRAINT chat_requestmessage_chat_id_54aa98af_fk_chat_requestchat_id FOREIGN KEY (chat_id) REFERENCES public.chat_requestchat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chat_requestmessage chat_requestmessage_request_id_2d05494c_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.chat_requestmessage
    ADD CONSTRAINT chat_requestmessage_request_id_2d05494c_fk_film_plac FOREIGN KEY (request_id) REFERENCES public.film_places_filmrequest(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacescomment film_places_filmplac_answer_id_comment_id_82f3d057_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment
    ADD CONSTRAINT film_places_filmplac_answer_id_comment_id_82f3d057_fk_film_plac FOREIGN KEY (answer_id_comment_id) REFERENCES public.film_places_filmplacescomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces_category film_places_filmplac_categoryfilmplaces_i_d3a28e0e_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_category
    ADD CONSTRAINT film_places_filmplac_categoryfilmplaces_i_d3a28e0e_fk_film_plac FOREIGN KEY (categoryfilmplaces_id) REFERENCES public.film_places_categoryfilmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces_category film_places_filmplac_filmplaces_id_3e85da19_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_category
    ADD CONSTRAINT film_places_filmplac_filmplaces_id_3e85da19_fk_film_plac FOREIGN KEY (filmplaces_id) REFERENCES public.film_places_filmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces_place_image film_places_filmplac_filmplaces_id_4c4a2cb3_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_place_image
    ADD CONSTRAINT film_places_filmplac_filmplaces_id_4c4a2cb3_fk_film_plac FOREIGN KEY (filmplaces_id) REFERENCES public.film_places_filmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces_place_image film_places_filmplac_image_id_986da258_fk_gallery_i; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces_place_image
    ADD CONSTRAINT film_places_filmplac_image_id_986da258_fk_gallery_i FOREIGN KEY (image_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces film_places_filmplac_main_photo_id_9cf1199a_fk_gallery_i; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces
    ADD CONSTRAINT film_places_filmplac_main_photo_id_9cf1199a_fk_gallery_i FOREIGN KEY (main_photo_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacescomment film_places_filmplac_place_id_3dcaf5ac_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment
    ADD CONSTRAINT film_places_filmplac_place_id_3dcaf5ac_fk_film_plac FOREIGN KEY (place_id) REFERENCES public.film_places_filmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaceslike film_places_filmplac_place_id_6ad4769d_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaceslike
    ADD CONSTRAINT film_places_filmplac_place_id_6ad4769d_fk_film_plac FOREIGN KEY (place_id) REFERENCES public.film_places_filmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacesfavorite film_places_filmplac_place_id_ba240d62_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacesfavorite
    ADD CONSTRAINT film_places_filmplac_place_id_ba240d62_fk_film_plac FOREIGN KEY (place_id) REFERENCES public.film_places_filmplaces(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaceslike film_places_filmplac_profile_id_07af7f5f_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaceslike
    ADD CONSTRAINT film_places_filmplac_profile_id_07af7f5f_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplaces film_places_filmplac_profile_id_3aaf61f0_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplaces
    ADD CONSTRAINT film_places_filmplac_profile_id_3aaf61f0_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacesfavorite film_places_filmplac_profile_id_94c8a44e_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacesfavorite
    ADD CONSTRAINT film_places_filmplac_profile_id_94c8a44e_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacescomment film_places_filmplac_quote_id_id_fe7944ef_fk_film_plac; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment
    ADD CONSTRAINT film_places_filmplac_quote_id_id_fe7944ef_fk_film_plac FOREIGN KEY (quote_id_id) REFERENCES public.film_places_filmplacescomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmplacescomment film_places_filmplac_sender_comment_id_061c4cd3_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmplacescomment
    ADD CONSTRAINT film_places_filmplac_sender_comment_id_061c4cd3_fk_accounts_ FOREIGN KEY (sender_comment_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmrequest film_places_filmrequ_profile_id_da6efa18_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmrequest
    ADD CONSTRAINT film_places_filmrequ_profile_id_da6efa18_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_filmrequest film_places_filmrequ_receiver_profile_id_eeb13afe_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_filmrequest
    ADD CONSTRAINT film_places_filmrequ_receiver_profile_id_eeb13afe_fk_accounts_ FOREIGN KEY (receiver_profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: film_places_notauthfilmrequest film_places_notauthf_receiver_profile_id_1fa89e32_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.film_places_notauthfilmrequest
    ADD CONSTRAINT film_places_notauthf_receiver_profile_id_1fa89e32_fk_accounts_ FOREIGN KEY (receiver_profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_album gallery_album_main_photo_id_id_b28832d5_fk_gallery_image_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_album
    ADD CONSTRAINT gallery_album_main_photo_id_id_b28832d5_fk_gallery_image_id FOREIGN KEY (main_photo_id_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_album gallery_album_profile_id_bd3955ac_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_album
    ADD CONSTRAINT gallery_album_profile_id_bd3955ac_fk_accounts_profile_id FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery_album gallery_gallery_album_album_id_6eda7942_fk_gallery_album_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_album
    ADD CONSTRAINT gallery_gallery_album_album_id_6eda7942_fk_gallery_album_id FOREIGN KEY (album_id) REFERENCES public.gallery_album(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery_album gallery_gallery_album_gallery_id_35e407e4_fk_gallery_gallery_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_album
    ADD CONSTRAINT gallery_gallery_album_gallery_id_35e407e4_fk_gallery_gallery_id FOREIGN KEY (gallery_id) REFERENCES public.gallery_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery_category gallery_gallery_cate_gallery_id_5533916e_fk_gallery_g; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_category
    ADD CONSTRAINT gallery_gallery_cate_gallery_id_5533916e_fk_gallery_g FOREIGN KEY (gallery_id) REFERENCES public.gallery_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery_category gallery_gallery_cate_specialization_id_63cf984f_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery_category
    ADD CONSTRAINT gallery_gallery_cate_specialization_id_63cf984f_fk_accounts_ FOREIGN KEY (specialization_id) REFERENCES public.accounts_specialization(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery gallery_gallery_gallery_image_id_0fd2be9f_fk_gallery_image_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery
    ADD CONSTRAINT gallery_gallery_gallery_image_id_0fd2be9f_fk_gallery_image_id FOREIGN KEY (gallery_image_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallery gallery_gallery_profile_id_f7b1a984_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallery
    ADD CONSTRAINT gallery_gallery_profile_id_f7b1a984_fk_accounts_profile_id FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerycomment gallery_gallerycomme_answer_id_comment_id_aa8ae339_fk_gallery_g; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment
    ADD CONSTRAINT gallery_gallerycomme_answer_id_comment_id_aa8ae339_fk_gallery_g FOREIGN KEY (answer_id_comment_id) REFERENCES public.gallery_gallerycomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerycomment gallery_gallerycomme_gallery_id_80df8aba_fk_gallery_g; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment
    ADD CONSTRAINT gallery_gallerycomme_gallery_id_80df8aba_fk_gallery_g FOREIGN KEY (gallery_id) REFERENCES public.gallery_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerycomment gallery_gallerycomme_quote_id_id_ef5aba5b_fk_gallery_g; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment
    ADD CONSTRAINT gallery_gallerycomme_quote_id_id_ef5aba5b_fk_gallery_g FOREIGN KEY (quote_id_id) REFERENCES public.gallery_gallerycomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerycomment gallery_gallerycomme_sender_comment_id_e72e5ac6_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerycomment
    ADD CONSTRAINT gallery_gallerycomme_sender_comment_id_e72e5ac6_fk_accounts_ FOREIGN KEY (sender_comment_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_galleryfavorite gallery_galleryfavor_gallery_id_bccfcafc_fk_gallery_g; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_galleryfavorite
    ADD CONSTRAINT gallery_galleryfavor_gallery_id_bccfcafc_fk_gallery_g FOREIGN KEY (gallery_id) REFERENCES public.gallery_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_galleryfavorite gallery_galleryfavor_profile_id_4ad1ef4b_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_galleryfavorite
    ADD CONSTRAINT gallery_galleryfavor_profile_id_4ad1ef4b_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerylike gallery_gallerylike_gallery_id_6b9da5a3_fk_gallery_gallery_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerylike
    ADD CONSTRAINT gallery_gallerylike_gallery_id_6b9da5a3_fk_gallery_gallery_id FOREIGN KEY (gallery_id) REFERENCES public.gallery_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_gallerylike gallery_gallerylike_profile_id_4980571a_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_gallerylike
    ADD CONSTRAINT gallery_gallerylike_profile_id_4980571a_fk_accounts_profile_id FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_image gallery_image_profile_id_0afef851_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_image
    ADD CONSTRAINT gallery_image_profile_id_0afef851_fk_accounts_profile_id FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessioncomment gallery_photosession_answer_id_comment_id_0570198c_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment
    ADD CONSTRAINT gallery_photosession_answer_id_comment_id_0570198c_fk_gallery_p FOREIGN KEY (answer_id_comment_id) REFERENCES public.gallery_photosessioncomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosession_photos gallery_photosession_image_id_651652cd_fk_gallery_i; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession_photos
    ADD CONSTRAINT gallery_photosession_image_id_651652cd_fk_gallery_i FOREIGN KEY (image_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosession gallery_photosession_main_photo_id_dddb8bef_fk_gallery_image_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession
    ADD CONSTRAINT gallery_photosession_main_photo_id_dddb8bef_fk_gallery_image_id FOREIGN KEY (main_photo_id) REFERENCES public.gallery_image(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessionlike gallery_photosession_photo_session_id_3ae0d312_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionlike
    ADD CONSTRAINT gallery_photosession_photo_session_id_3ae0d312_fk_gallery_p FOREIGN KEY (photo_session_id) REFERENCES public.gallery_photosession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessioncomment gallery_photosession_photo_session_id_d4b5267d_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment
    ADD CONSTRAINT gallery_photosession_photo_session_id_d4b5267d_fk_gallery_p FOREIGN KEY (photo_session_id) REFERENCES public.gallery_photosession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessionfavorite gallery_photosession_photo_session_id_fed07a7d_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionfavorite
    ADD CONSTRAINT gallery_photosession_photo_session_id_fed07a7d_fk_gallery_p FOREIGN KEY (photo_session_id) REFERENCES public.gallery_photosession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosession_photos gallery_photosession_photosession_id_83c87951_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession_photos
    ADD CONSTRAINT gallery_photosession_photosession_id_83c87951_fk_gallery_p FOREIGN KEY (photosession_id) REFERENCES public.gallery_photosession(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessionfavorite gallery_photosession_profile_id_6acb43c2_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionfavorite
    ADD CONSTRAINT gallery_photosession_profile_id_6acb43c2_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosession gallery_photosession_profile_id_96e6036e_fk_accounts_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession
    ADD CONSTRAINT gallery_photosession_profile_id_96e6036e_fk_accounts_profile_id FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessionlike gallery_photosession_profile_id_cf5c3f32_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessionlike
    ADD CONSTRAINT gallery_photosession_profile_id_cf5c3f32_fk_accounts_ FOREIGN KEY (profile_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessioncomment gallery_photosession_quote_id_id_b2241806_fk_gallery_p; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment
    ADD CONSTRAINT gallery_photosession_quote_id_id_b2241806_fk_gallery_p FOREIGN KEY (quote_id_id) REFERENCES public.gallery_photosessioncomment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosessioncomment gallery_photosession_sender_comment_id_97d27382_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosessioncomment
    ADD CONSTRAINT gallery_photosession_sender_comment_id_97d27382_fk_accounts_ FOREIGN KEY (sender_comment_id) REFERENCES public.accounts_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: gallery_photosession gallery_photosession_session_category_id_0ca02969_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: photo_user
--

ALTER TABLE ONLY public.gallery_photosession
    ADD CONSTRAINT gallery_photosession_session_category_id_0ca02969_fk_accounts_ FOREIGN KEY (session_category_id) REFERENCES public.accounts_specialization(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

