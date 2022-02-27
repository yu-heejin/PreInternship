from pickle import GET
from flask import Flask, request, Response
import numpy as np
import cv2
import base64
from base64 import encodebytes
import io
from PIL import Image
import matplotlib.pyplot as plt
import dlib

    
# Initialize the Flask application
app = Flask(__name__)

@app.route(r'/api/face_swap', methods=['POST'])

def face_swap():
    r = request
    
   
    face = base64.b64decode(r.json.get('face'))   
    face = Image.open(io.BytesIO(face))

    body = base64.b64decode(r.json.get('body'))
    body = Image.open(io.BytesIO(body))

   
    face = np.array(face)
    body = np.array(body)

  
    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    body_gray = cv2.cvtColor(body, cv2.COLOR_BGR2GRAY)

  
    height, width = face_gray.shape
    mask = np.zeros((height, width), np.uint8)

    height, width, channels = body.shape

  
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(r"C:\Users\82102\Desktop\faceswap_project2\openCV_Project\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat")

    rect = detector(face_gray)[0]

   
    landmarks = predictor(face_gray, rect)
    landmarks_points = [] 

    def get_landmarks(landmarks, landmarks_points):
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_points.append((x, y))

    get_landmarks(landmarks, landmarks_points)

    points = np.array(landmarks_points, np.int32)

    convexhull = cv2.convexHull(points) 

    face_cp = face.copy()

    face_image_1 = cv2.bitwise_and(face, face, mask=mask)

    rect = cv2.boundingRect(convexhull)

    subdiv = cv2.Subdiv2D(rect) # Creates an instance of Subdiv2D
    subdiv.insert(landmarks_points) # Insert points into subdiv
    triangles = subdiv.getTriangleList()
    triangles = np.array(triangles, dtype=np.int32)

    indexes_triangles = []
    face_cp = face.copy()

    def get_index(arr):
        index = 0
        if arr[0]:
            index = arr[0][0]
        return index

    for triangle in triangles :

        # Gets the vertex of the triangle
        pt1 = (triangle[0], triangle[1])
        pt2 = (triangle[2], triangle[3])
        pt3 = (triangle[4], triangle[5])

        # Draws a line for each side of the triangle
        cv2.line(face_cp, pt1, pt2, (255, 255, 255), 3,  0)
        cv2.line(face_cp, pt2, pt3, (255, 255, 255), 3,  0)
        cv2.line(face_cp, pt3, pt1, (255, 255, 255), 3,  0)

        index_pt1 = np.where((points == pt1).all(axis=1))
        index_pt1 = get_index(index_pt1)
        index_pt2 = np.where((points == pt2).all(axis=1))
        index_pt2 = get_index(index_pt2)
        index_pt3 = np.where((points == pt3).all(axis=1))
        index_pt3 = get_index(index_pt3)

    
        if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
            vertices = [index_pt1, index_pt2, index_pt3]
            indexes_triangles.append(vertices)


    rect2 = detector(body_gray)[0]

 
    landmarks_2 = predictor(body_gray, rect2)
    landmarks_points2 = []

  
    get_landmarks(landmarks_2, landmarks_points2)

   
    points2 = np.array(landmarks_points2, np.int32)
    convexhull2 = cv2.convexHull(points2)

    body_cp = body.copy()

    lines_space_new_face = np.zeros((height, width, channels), np.uint8)
    body_new_face = np.zeros((height, width, channels), np.uint8)

    height, width = face_gray.shape
    lines_space_mask = np.zeros((height, width), np.uint8)


    for triangle in indexes_triangles:

        
        pt1 = landmarks_points[triangle[0]]
        pt2 = landmarks_points[triangle[1]]
        pt3 = landmarks_points[triangle[2]]

        
        (x, y, widht, height) = cv2.boundingRect(np.array([pt1, pt2, pt3], np.int32))
        cropped_triangle = face[y: y+height, x: x+widht]
        cropped_mask = np.zeros((height, widht), np.uint8)

       
        points = np.array([[pt1[0]-x, pt1[1]-y], [pt2[0]-x, pt2[1]-y], [pt3[0]-x, pt3[1]-y]], np.int32)
        cv2.fillConvexPoly(cropped_mask, points, 255)

        
        cv2.line(lines_space_mask, pt1, pt2, 255)
        cv2.line(lines_space_mask, pt2, pt3, 255)
        cv2.line(lines_space_mask, pt1, pt3, 255)

        lines_space = cv2.bitwise_and(face, face, mask=lines_space_mask)

        

        pt1 = landmarks_points2[triangle[0]]
        pt2 = landmarks_points2[triangle[1]]
        pt3 = landmarks_points2[triangle[2]]

      
        (x, y, widht, height) = cv2.boundingRect(np.array([pt1, pt2, pt3], np.int32))
        cropped_mask2 = np.zeros((height,widht), np.uint8)

  
        points2 = np.array([[pt1[0]-x, pt1[1]-y], [pt2[0]-x, pt2[1]-y], [pt3[0]-x, pt3[1]-y]], np.int32)
        cv2.fillConvexPoly(cropped_mask2, points2, 255)

     
        points =  np.float32(points)
        points2 = np.float32(points2)
        M = cv2.getAffineTransform(points, points2) 
        dist_triangle = cv2.warpAffine(cropped_triangle, M, (widht, height))
        dist_triangle = cv2.bitwise_and(dist_triangle, dist_triangle, mask=cropped_mask2)

        
        body_new_face_rect_area = body_new_face[y: y+height, x: x+widht]
        body_new_face_rect_area_gray = cv2.cvtColor(body_new_face_rect_area, cv2.COLOR_BGR2GRAY)

        
        masked_triangle = cv2.threshold(body_new_face_rect_area_gray, 1, 255, cv2.THRESH_BINARY_INV)
        dist_triangle = cv2.bitwise_and(dist_triangle, dist_triangle, mask=masked_triangle[1])

     
        body_new_face_rect_area = cv2.add(body_new_face_rect_area, dist_triangle)
        body_new_face[y: y+height, x: x+widht] = body_new_face_rect_area

    body_face_mask = np.zeros_like(body_gray)
    body_head_mask = cv2.fillConvexPoly(body_face_mask, convexhull2, 255)
    body_face_mask = cv2.bitwise_not(body_head_mask)

    body_maskless = cv2.bitwise_and(body, body, mask=body_face_mask)
    result = cv2.add(body_maskless, body_new_face)

  
    (x, y, widht, height) = cv2.boundingRect(convexhull2)
    center_face2 = (int((x+x+widht)/2), int((y+y+height)/2))

    new = cv2.seamlessClone(result, body, body_head_mask, center_face2, cv2.NORMAL_CLONE)
    

    new = Image.fromarray(new)
    byte_arr = io.BytesIO()
    new.save(byte_arr, format='PNG') 
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') 
    
    return {'image': encoded_img}



app.run(host="0.0.0.0", port=5000)





