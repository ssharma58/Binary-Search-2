class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash= {}
        thash={}
        if (len(s)==0 or s==None ):
                return -1
        for i in range(len(s)):
            schar= s[i]
            tchar=t[i]
            if(schar in shash):
                if(shash.get(schar)!=tchar):
                    return False
                
                
            else:
                shash[schar]=tchar
                
            
            if (tchar in thash):
                if(thash.get(tchar)!=schar):
                    return False
                
            else:
                thash[tchar]=schar
        return True
            
            
        