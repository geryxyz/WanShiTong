from processor import Processor
from Article import Article
from conditionss.Filter import Contains
from conditionss.Logic import And, Or
from typing import List

if __name__ == '__main__':
    '''
    ap = Processor(Article) -> létrehozza és lekéri az összes Article-t
    articles[] = ap.get(Filters = ?, Logic = ?, Order = ?, Pagination = ?) -> önálló metódusként is működjenek ezek
    
    
    '''
    p = Processor(Article) #First, we have to make a Processor and add the entry type in the parameter

    p.filter(Contains(Article.__fields__['author'], "Marg"), Contains(Article.__fields__['title'], "Kin"))
    #And we can start filtering our data
    p.logic(And())
    #Make one logical
    result = p.get_result()
    print(result)

