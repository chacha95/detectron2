class Category:
    """
    Category 정보 class
    staticmethod를 이용해 
    전역적으로 사용 가능한 class
    """
    cat_all_set = None
    cat_in_set = []
    cat_no_set = []

    @staticmethod
    def category_in(cat_names):
        """
        (category name)들을 받아 
        (category name)에 해당하는 
        (category 번호)를 
        list에 저장
        
        Args:
            cat_names (list): category name list
        """
        # 품목에 있는 Category 설정
        for cat_name in cat_names:
            Category.cat_in_set.append(Category.cat_all_set[cat_name])
        
        # 품목에 없는 Category 설정
        for cat_name in cat_names:
            if cat_name not in Category.cat_in_set:
                Category.cat_no_set.append(Category.cat_all_set[cat_name])
        
        Category.cat_all_set = set(Category.cat_all_set.values())
        Category.cat_in_set = set(Category.cat_in_set)
        Category.cat_no_set = Category.cat_all_set - Category.cat_in_set

    @staticmethod
    def category_init(cat_all):
        """
        (category list)를 None으로 초기화
        """
        Category.cat_all_set = cat_all
        Category.cat_in_set = []
        Category.cat_no_set = []
