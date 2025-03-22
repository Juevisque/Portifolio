import cv2


vavaPrint_img = cv2.imread("robo valorant.png", cv2.IMREAD_UNCHANGED)
cabezinha_img = cv2.imread("cabizinha.png", cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(vavaPrint_img,cabezinha_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("Resultado", result)
cv2.waitKey()
cv2.destroyAllWindows()