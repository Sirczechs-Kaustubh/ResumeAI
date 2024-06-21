import yaml

# Function to load YAML data
def load_yaml_data(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

resume_data = load_yaml_data('template.yaml')

# function to modify the experience details
def modify_experience_details(resume_data, company_name, action,
                              index=None, new_detail=None, new_info=None):
    """
    Modify the experience details by adding or removing points.

    Parameters:
        resume_data (dict): The resume data loaded from YAML.
        company_name (str): The company name to identify the correct experience entry.
        action (str): 'add' to add a new detail, 'delete' to delete a detail, 'replace' to replace a detail from user input.
        index (int): The index to delete or insert the detail at.
        new_detail (str): The new detail to add, required if action is 'add'.
        new_info (list) : The points to be added are presented in a list.
    """
    # Find the right experience entry
    for experience in resume_data['experience']:
        if experience['company'] == company_name:
            if action == 'add' and new_detail is not None:
                # Add new detail at the specified index or append if no index provided
                if index is not None:
                    experience['details'].insert(index, new_detail)
                else:
                    experience['details'].append(new_detail)
            elif action == 'delete' and index is not None:
                # Delete detail at specified index
                del experience['details'][index]
                # this will replace the text
            elif action == 'replace' and new_info is not None:
                experience['details'] = new_info
            break




# Example Implementation
modify_experience_details(resume_data, 'Petbiotech', 'add', new_detail='Implemented new ML model for forecasting.')
modify_experience_details(resume_data, 'Petbiotech', 'delete', index=0)

