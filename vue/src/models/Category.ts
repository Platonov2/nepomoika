/**
 * Класс категории.
 */
export default interface Category {

    /**
     * Все поля являются отображением получаемой с бэкенда модели класса Category.
     */
    category_id: number;
    category_name: string;
    root_category_id: number;
    children_categories_id: number[];
    is_leaf: boolean;
}