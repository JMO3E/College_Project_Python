class Register:
    def __init__(self, configFileName = '', courseName = '', studFileName = '', evaluationCount = 0):

        self._configFileName = configFileName
        self._courseName = courseName
        self._studFileName = studFileName
        self._evaluationCount = evaluationCount

    '''
        Configuration File Name
    '''
    # Setter
    def setConfigFileName(self, value):
        self._configFileName = value

    #Getter
    def getConfigFileName(self):
        return self._configFileName

    '''
        Course Name
    '''
    # Setter
    def setCourseName(self, value):
        self._courseName = value

    # Getter
    def getCourseName(self):
        return self._courseName

    '''
        Student File Name
    '''
    # Setter
    def setStudFileName(self, value):
        self._studFileName = value

    # Getter
    def getStudFileName(self):
        return self._studFileName

    '''
        Evaluation Count
    '''
    # Setter
    def setEvaluationCount(self, value):
        self._evaluationCount = value

    # Getter
    def getEvaluationCount(self):
        return self._evaluationCount
