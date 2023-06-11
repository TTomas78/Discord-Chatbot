class TemplateProfile:
    ''' This a template for an user profile, this must contain all the neccesary information to run the assistant on some of the roles'''
    
    data = None
    
    def __init__(self):
        pass

class SystemProfile(TemplateProfile):
    '''Fill this with the data of the user that is going to be the system'''

    job_data = '''
    Carlos is a 20-year-old man born in Argentina.
    He is in charge of a team made up of:
    Pepe and Jose who deal with the QA process
    Sebastian and Dario who deal with booking flow
    Ezequiel, German and Alberto take care of the backend
    The two clients of Carlos's project are called Tesla and SpaceX
    The feature you are currently working on is called calendar and it would be ready to upload if Tesla sends you the translations.
    '''

class UserProfile(TemplateProfile):

    job_data = '''
    Juan is a man who currently lives in Italy.
    Work in the company as a project manager.
    '''