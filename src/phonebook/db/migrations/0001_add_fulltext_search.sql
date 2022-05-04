ALTER TABLE contacts
    ADD COLUMN __fulltext__ TSVECTOR
        GENERATED ALWAYS AS
        (
            to_tsvector('Italian', firstname || ' ' ||
                                   COALESCE(lastname, '') || ' ' ||
                                   COALESCE(address, '') || ' ' ||
                                   COALESCE(comment, ''))
        ) STORED;

CREATE INDEX contacts_fulltext_idx ON contacts USING gin (__fulltext__);
