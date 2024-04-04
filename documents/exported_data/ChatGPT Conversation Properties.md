# ChatGPT Conversation Properties

Here is a comprehensive hierarchical list of the parameters, keys, properties, and their corresponding values, types, and descriptions used across the 7 conversations in the provided JSON format:

- `title` *(string)*  
  The title or subject of the conversation.

- `create_time` *(number)*  
  The Unix timestamp indicating when the conversation was created.

- `update_time` *(number)*  
  The Unix timestamp indicating when the conversation was last updated.

- `mapping` *(object)*  
  Contains the mapping of nodes within the conversation.
  - `id` *(string)*  
    The unique identifier for each node in the conversation.
  - `message` *(object)*  
    Represents a message within a node.
    - `id` *(string)*  
      The unique identifier for the message.
    - `author` *(object)*  
      Contains information about the author of the message.
      - `role` *(string)*  
        The role of the author (e.g., `"system", "user", "assistant", "tool"`).
      - `name` *(string or null)*  
        The name of the author, if available.
      - `metadata` *(object)*  
        Additional metadata associated with the author.
    - `create_time` *(number or null)*  
      The Unix timestamp indicating when the message was created.
    - `update_time` *(number or null)*  
      The Unix timestamp indicating when the message was last updated.
    - `content` *(object)*  
      Contains the content of the message.
      - `content_type` *(string)*  
        The type of content (e.g., `"text", "code", "multimodal_text", "execution_output", "tether_browsing_display", "tether_quote"`).
      - `parts` *(array)*  
        An array of strings or objects representing the parts of the message content.
        - `content_type` *(string)*  
          The type of content for each part (e.g., `"text", "image_asset_pointer"`).
        - `asset_pointer` *(string)*  
          The pointer to the image asset.
        - `size_bytes` *(number)*  
          The size of the image asset in bytes.
        - `width` *(number)*  
          The width of the image asset.
        - `height` *(number)*  The height of the image asset.
        - `fovea` *(number or null)*  The fovea of the image asset, if applicable.
        - `metadata` *(object or null)*: Additional metadata associated with the image asset.
          - `dalle` *(object)*  Metadata specific to DALL-E generated images.
            - `gen_id` *(string)*  The generation ID of the DALL-E image.
            - `prompt` *(string)*  The prompt used to generate the DALL-E image.
            - `seed` *(number)*  The seed value used for generating the DALL-E image.
            - `parent_gen_id` *(string or null)*  The parent generation ID, if applicable.
            - `edit_op` *(string or null)*  The edit operation applied to the DALL-E image, if applicable.
            - `serialization_title` *(string)*  The title of the DALL-E image serialization.
      - `language` *(string)*  The programming language of the code content.
      - `text` *(string)*  The text content of the message.
      - `url` *(string)*  The URL associated with the tether browsing display.
      - `domain` *(string)*  The domain associated with the tether browsing display.
      - `title` *(string)*  The title of the tether browsing display.
      - `result` *(string)*  The result of the tether browsing display.
      - `summary` *(string or null)*  The summary of the tether browsing display.
      - `assets` *(array)*  An array of assets associated with the tether browsing display.
    - `status` *(string)*  The status of the message (e.g., "finished_successfully", "in_progress").
    - `end_turn` *(boolean or null)*: Indicates whether the message ends the current turn.
    - `weight` *(number)*  The weight or importance of the message within the conversation.
    - `metadata` *(object)*  Additional metadata associated with the message.
      - `finish_details` (object, optional): Contains details about the finishing of the message.
        - `type` *(string)*  The type of finishing (e.g., "stop", "max_tokens", "interrupted").
        - `stop_tokens` *(array)*  An array of integers representing the stop tokens.
      - `citations` *(array)*  An array of citation objects.
        - `start_ix` *(number)*  The starting index of the citation in the message content.
        - `end_ix` *(number)*  The ending index of the citation in the message content.
        - `citation_format_type` *(string)*  The format type of the citation (e.g., "tether_og").
        - `metadata` *(object)*  Metadata associated with the citation.
          - `type` *(string)*  The type of the cited content (e.g., "webpage").
          - `title` *(string)*  The title of the cited content.
          - `url` *(string)*  The URL of the cited content.
          - `text` *(string)*  The text content of the citation.
          - `pub_date` *(string or null)*  The publication date of the cited content.
          - `extra` *(object or null)*: Extra information associated with the citation.
            - `evidence_text` *(string)*  The evidence text for the citation.
            - `cited_message_idx` *(number)*  The index of the cited message.
            - `search_result_idx` *(number or null)*  The index of the search result, if applicable.
      - `gizmo_id` *(string or null)*  The identifier for the gizmo used in the message, if applicable.
      - `is_complete` *(boolean)*: Indicates whether the message is complete.
      - `is_visually_hidden_from_conversation` *(boolean)*: Indicates whether the message is visually hidden from the conversation.
      - `message_type` *(string or null)*  The type of the message.
      - `model_slug` *(string)*  The slug identifier for the model used to generate the message.
      - `requested_model_slug` *(string, optional)*: The requested slug identifier for the model.
      - `default_model_slug` *(string)*  The default slug identifier for the model.
      - `pad` *(string)*  The padding string for the message.
      - `parent_id` *(string)*  The identifier of the parent message.
      - `request_id` *(string)*  The identifier for the request associated with the message.
      - `timestamp_` *(string)*  The timestamp associated with the message.
      - `attachments` *(array)*  An array of attachment objects associated with the message.
        - `size` *(number)*  The size of the attachment in bytes.
        - `name` *(string)*  The name of the attachment file.
        - `height` *(number)*  The height of the attachment, if applicable.
        - `id` *(string)*  The unique identifier for the attachment.
        - `width` *(number)*  The width of the attachment, if applicable.
      - `rebase_system_message` *(boolean)*: Indicates whether the system message should be rebased.
      - `_cite_metadata` *(object)*  Metadata associated with citations in the message.
        - `citation_format` *(object)*  The citation format used.
          - `name` *(string)*  The name of the citation format.
          - `regex` *(string)*  The regular expression pattern for the citation format.
        - `metadata_list` *(array)*  An array of metadata objects for each citation.
          - `type` *(string)*  The type of the cited content (e.g., "webpage").
          - `title` *(string)*  The title of the cited content.
          - `url` *(string)*  The URL of the cited content.
          - `text` *(string)*  The text content of the citation.
          - `pub_date` *(string or null)*  The publication date of the cited content.
          - `extra` *(object or null)*: Extra information associated with the citation.
        - `original_query` *(string or null)*  The original query associated with the citations.
      - `command` *(string)*  The command associated with the message (e.g., "search", "mclick").
      - `args` *(array)*  An array of arguments associated with the command.
      - `is_visually_hidden_from_conversation` *(boolean)*: Indicates whether the message is visually hidden from the conversation.
    - `recipient` *(string)*  The recipient of the message (e.g., "all", "dalle.text2im", "browser", "bio", "python").
  - `parent` *(string or null)*  The identifier of the parent node.
  - `children` *(array)*  An array of identifiers representing the child nodes.

- `moderation_results` *(array)*  An array of moderation results for the conversation.

- `current_node` *(string)*  The identifier of the current node in the conversation.

- `plugin_ids` *(null)*: Plugin identifiers associated with the conversation, if applicable.

- `conversation_id` *(string)*  The unique identifier for the conversation.

- `conversation_template_id` *(null)*: The identifier for the conversation template, if applicable.

- `gizmo_id` *(null)*: The identifier for the gizmo used in the conversation, if applicable.

- `is_archived` *(boolean)*: Indicates whether the conversation is archived.

- `safe_urls` *(array)*  An array of safe URLs associated with the conversation.

- `default_model_slug` *(string)*  The default slug identifier for the model used in the conversation.

- `id` *(string)*  The unique identifier for the conversation.

This hierarchical list provides a structured overview of the parameters, keys, properties, and their corresponding values, types, and descriptions used in the provided JSON data. It captures the relationships between different elements and offers a clear understanding of their purposes and functionalities within the context of the conversations.
