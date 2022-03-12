ALTER TABLE contacts
    ADD COLUMN __fulltext__ TSVECTOR
        GENERATED ALWAYS AS
        (
            to_tsvector('english', firstname || ' ' ||
                                   COALESCE(lastname, '') || ' ' ||
                                   COALESCE(address, '') || ' ' ||
                                   COALESCE(comment, ''))
        ) STORED;
