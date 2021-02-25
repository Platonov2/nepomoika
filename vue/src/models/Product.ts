/**
 * Класс товара.
 */
export default interface Product {

    /**
     * Все поля являются отображением получаемой с бэкенда модели класса Product.
     */
    product_id: number;
    product_name: string;
    product_price: number;
    image_link: string;
    product_category_id: number;
}
