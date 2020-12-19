def filter_peer_list_by_priority_copy(filter_items=None, container=None, **kwargs):
    """
    Args:
        filter_items: priority
        container (CEF type: phantom container id)
    
    Returns a JSON-serializable object that implements the configured data paths:
        filtered_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    filtered_list = []
    phantom.debug(type(filter_items)) 
    phantom.debug(type(container))
    phantom.debug(container)
        
    # The filter terms should 
    peer_list_name = phantom.get_container(container)['data']["peer_list"]
    peer_list = phantom.get_list(peer_list_name)[2]  
    
    temp_filter_items = filter_items[0].split(',')
    temp_filter_items = [obj.strip() for obj in temp_filter_items]
        
    my_list = peer_list
    phantom.debug(my_list)
    phantom.debug(temp_filter_items)
    
    # Iterate through and filter the nested list based on the filter items
    for term in temp_filter_items:
        temp_list = [obj for obj in my_list if term.strip() in obj]
        phantom.debug(term) 
        filtered_list.extend(temp_list)

    phantom.debug(filtered_list)  
    outputs = {'filtered_list': filtered_list}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
